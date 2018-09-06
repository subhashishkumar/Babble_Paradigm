# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.db import models

EMP_TYPE = (
    ('Regular', 'Regular'),
    ('Contract', 'Contract'),
)

ACCD_TYPE = (
    ('Fatal', 'Fatal'),
    ('Reportable', 'Reportable'),
    ('Non-Reportable', 'Non-Reportable'),
    ('First-Aid', 'First-Aid'),
)

SHIFT_TYPE = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('G', 'G'),
)

common_list = [
    ('Fall of material', 'Fall of material'),
    ('Material handling', 'Material handling'),
    ('Road incident', 'Road incident'),
    ('Slip', 'Slip'),
    ('Fall of person', 'Fall of person'),
    ('Burn', 'Burn'),
    ('Electrocution', 'Electrocution'),
    ('Gas exposure', 'Gas exposure'),
    ('Hit/Caught/Pressed', 'Hit/Caught/Pressed'),
]
other_list = [
    ('Violation of SOPs', 'Violation of SOPs'),
    ('Violation of SMPs', 'Violation of SMPs'),
    ('BBS Aspects', 'BBS Aspects'),
    ('Equipment Failure', 'Equipment Failure'),
]

causes_list = (
    ('Common Causes:', tuple(common_list)),
    ('Others:', tuple(other_list)),
)


# Create your models here.
class emp_details(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    unit_name = models.CharField(max_length=30, verbose_name='Unit Name')
    emp_id = models.CharField(primary_key=True, max_length=15, verbose_name='Employee ID')
    emp_type = models.CharField(max_length=20, choices=EMP_TYPE, default='Regular', verbose_name='Employee Type')
    emp_name = models.CharField(max_length=30, verbose_name='Employee Name')
    age = models.PositiveSmallIntegerField(default='21', verbose_name='Age')
    dept = models.CharField(max_length=20, verbose_name='Department')
    shift = models.CharField(max_length=5, choices=SHIFT_TYPE, default='A', verbose_name='Shift')

    class Meta:
        verbose_name_plural = 'Employee Details'

    def __unicode__(self):
        return self.emp_id


class accd_details(models.Model):
    accd_id = models.AutoField(primary_key=True, verbose_name='Accident ID')
    accd_type = models.CharField(max_length=30, choices=ACCD_TYPE, default='Fatal', verbose_name='Accident Type')
    date = models.DateTimeField(verbose_name='Date and Time')
    emp_id = models.ForeignKey(emp_details, related_name='accd_emp_id', on_delete=models.CASCADE)
    cause = models.CharField(max_length=100, choices=causes_list, default='Slip', verbose_name='Accident Cause')
    narrative = models.TextField(verbose_name='Narrative')
    learning_point = models.CharField(max_length=50, verbose_name='Learning Point', blank=True)

    class Meta:
        verbose_name_plural = 'Accident Details'

    def __unicode__(self):
        return unicode(self.accd_id) or u''


class AllAccident(models.Model):
    UnitName = models.CharField(max_length=30, verbose_name='Unit Name', db_column='unit_name')
    AccdId = models.OneToOneField(
        'accd_details', primary_key=True, on_delete=models.DO_NOTHING, verbose_name='Accident ID', db_column='accd_id')
    AccdType = models.CharField(
        max_length=30, choices=ACCD_TYPE, default='Fatal', verbose_name='Accident Type', db_column='accd_type')
    Date = models.DateTimeField(verbose_name='Date and Time')
    EmpID = models.ForeignKey(
        'emp_details', on_delete=models.DO_NOTHING, verbose_name='Employee ID', db_column='emp_id')
    EmpName = models.CharField(max_length=30, verbose_name='Employee Name', db_column='emp_name')
    EmpType = models.CharField(
        max_length=10, choices=EMP_TYPE, default='Regular', verbose_name='Employee Type', db_column='emp_type')
    Department = models.CharField(max_length=20, db_column='dept')
    Shift = models.CharField(max_length=20, choices=SHIFT_TYPE, default='A', db_column='shift')
    Cause = models.CharField(max_length=100, choices=causes_list, default='Slip', db_column='cause')
    Narrative = models.TextField(verbose_name='Narrative', db_column='narrative')
    LearningPoint = models.CharField(
        max_length=50, verbose_name='Learning Point', blank=True, db_column='learning_point')

    class Meta:
        managed = False
        db_table = 'emp_accd_view'

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.UnitName, self.AccdType, self.EmpType)


class manhours(models.Model):
    unit_name = models.CharField(max_length=30, verbose_name='Unit Name')
    date = models.DateField(verbose_name='Date')
    manhours_worked_regular = models.BigIntegerField(verbose_name='Manhours Worked Regular', default=0)
    manhours_worked_contract = models.BigIntegerField(verbose_name='Manhours Worked Contract', default=0)
    mandays_lost = models.IntegerField(verbose_name='Man-Days Lost')

    class Meta:
        verbose_name_plural = 'Manhours Details'

    def getMonthlyCounts(self):
        monthNumber = self.date.strftime('%m')
        tc = AllAccident.objects.filter(
            UnitName=self.unit_name, Date__month=monthNumber).defer("EmpName", "Narrative", "LearningPoint")
        fc = tc.filter(AccdType='Fatal').count()
        rc = tc.filter(AccdType='Reportable').count()
        nrc = tc.filter(AccdType='Non-Reportable').count()
        mw = self.manhours_worked_regular + self.manhours_worked_contract
        return fc, rc, nrc, mw

    @property
    def RLTIFR(self):
        fc, rc, nrc, manhours_worked = self.getMonthlyCounts()
        self.rltifr = (fc + rc) * 1000000
        self.rltifr = Decimal(self.rltifr) / manhours_worked
        return round(self.rltifr, 4)

    @property
    def LTIFR(self):
        fc, rc, nrc, manhours_worked = self.getMonthlyCounts()
        self.ltifr = (fc + rc + nrc) * 1000000
        self.ltifr = Decimal(self.ltifr) / manhours_worked
        return round(self.ltifr, 4)

    @property
    def SEVERITY_RATE(self):
        fc, rc, nrc, manhours_worked = self.getMonthlyCounts()
        self.severity_rate = self.mandays_lost * 1000000
        self.severity_rate = Decimal(self.severity_rate) / manhours_worked
        return round(self.severity_rate, 4)

    def __unicode__(self):
        return '{0} {1} {2} {3} {4}'.format(
            self.unit_name, self.date, self.manhours_worked_regular, self.manhours_worked_contract, self.mandays_lost,)
