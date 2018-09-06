# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import collections
from .filters import *
from .tables import *
from login.models import *
from InputForms.models import *
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
units_list = profile.objects.values_list('unit', flat=True).order_by("unit")[1:]
accd = AllAccident.objects.defer("EmpName", "Narrative", "LearningPoint")
accd_r = accd.filter(EmpType='Regular')
accd_c = accd.filter(EmpType='Contract')

accd_fa_r = accd_r.filter(AccdType='First-Aid')
accd_fa_c = accd_c.filter(AccdType='First-Aid')

accd_nr_r = accd_r.filter(AccdType='Non-Reportable')
accd_nr_c = accd_c.filter(AccdType='Non-Reportable')

accd_r_r = accd_r.filter(AccdType='Reportable')
accd_r_c = accd_c.filter(AccdType='Reportable')

accd_f_r = accd_r.filter(AccdType='Fatal')
accd_f_c = accd_c.filter(AccdType='Fatal')


dt_today = datetime.datetime.today()
tday = dt_today.day
wk = dt_today.isocalendar()[1]
mn = dt_today.month
yr = dt_today.year


def calculate_data_view(accd_reg, accd_contr):
    dt_reg = collections.OrderedDict()
    dt_contr = collections.OrderedDict()
    sum_type = collections.OrderedDict()
    for x in units_list:
        dt_reg[x] = accd_reg.filter(UnitName=x,).count()
        dt_contr[x] = accd_contr.filter(UnitName=x,).count()

    sum_reg = sum(dt_reg.values())
    sum_contr = sum(dt_contr.values())

    for x in units_list:
        sum_type[x] = dt_reg[x] + dt_contr[x]
    sum_total = sum(sum_type.values())
    type_list = zip(units_list, dt_reg.values(), dt_contr.values(), sum_type.values())

    return type_list, sum_reg, sum_contr, sum_total


@login_required(login_url='/users/login_user/')
def showtables(request):
    return render(request, 'ShowTables.html',)


@login_required(login_url='/users/login_user/')
def get_data_view(request, accdType):
    type_accd = accdType
    ar = []
    ac = []
    use_name = ""
    time_filter_type = ""
    sum_reg = ""
    sum_contr = ""
    sum_total = ""
    type_list = []

    if type_accd == "fatal":
        ar = accd_f_r
        ac = accd_f_c
        use_name = "Fatal"

    if type_accd == "first-aid":
        ar = accd_fa_r
        ac = accd_fa_c
        use_name = "First-Aid"

    if type_accd == "reportable":
        ar = accd_r_r
        ac = accd_r_c
        use_name = "Reportable"

    if type_accd == "non-reportable":
        ar = accd_nr_r
        ac = accd_nr_c
        use_name = "Non-Reportable"

    query = request.GET.get('time', 'today')
    if query == "today":
        accd_reg = ar.filter(Date__year=yr, Date__month=mn, Date__day=tday)
        accd_contr = ac.filter(Date__year=yr, Date__month=mn, Date__day=tday)
        type_list, sum_reg, sum_contr, sum_total = calculate_data_view(accd_reg, accd_contr)
        time_filter_type = "Today's"

    if query == "thisWeek":
        accd_reg = ar.filter(Date__year=yr, Date__week=wk)
        accd_contr = ac.filter(Date__year=yr, Date__week=wk)
        type_list, sum_reg, sum_contr, sum_total = calculate_data_view(accd_reg, accd_contr)
        time_filter_type = "This Week"

    if query == "thisMonth":
        accd_reg = ar.filter(Date__year=yr, Date__month=mn)
        accd_contr = ac.filter(Date__year=yr, Date__month=mn)
        type_list, sum_reg, sum_contr, sum_total = calculate_data_view(accd_reg, accd_contr)
        time_filter_type = "This Week"

    if query == "thisYear":
        accd_reg = ar.filter(Date__year=yr)
        accd_contr = ac.filter(Date__year=yr)
        type_list, sum_reg, sum_contr, sum_total = calculate_data_view(accd_reg, accd_contr)
        time_filter_type = "This Year"

    context = {
        # Genral Default Contexts
        'Header': use_name, 'pagetitle': use_name, 'time': time_filter_type,
        # Day Context
        'list': type_list, 'sum_reg': sum_reg, 'sum_contr': sum_contr, 'sum': sum_total,
    }

    return render(request, 'filterTable.html', context)


@login_required(login_url='/users/login_user/')
def year_wise_detailed(request):
    if request.method == 'GET':
        GetYear = request.GET.get('yearVal', yr)

        fa_year_r = accd_fa_r.filter(Date__year=GetYear)
        f_year_r = accd_f_r.filter(Date__year=GetYear)
        nr_year_r = accd_nr_r.filter(Date__year=GetYear)
        r_year_r = accd_r_r.filter(Date__year=GetYear)

        fa_year_c = accd_fa_c.filter(Date__year=GetYear)
        f_year_c = accd_f_c.filter(Date__year=GetYear)
        nr_year_c = accd_nr_c.filter(Date__year=GetYear)
        r_year_c = accd_r_c.filter(Date__year=GetYear)

        fa_year_reg = collections.OrderedDict()
        f_year_reg = collections.OrderedDict()
        nr_year_reg = collections.OrderedDict()
        r_year_reg = collections.OrderedDict()

        fa_year_contr = collections.OrderedDict()
        f_year_contr = collections.OrderedDict()
        nr_year_contr = collections.OrderedDict()
        r_year_contr = collections.OrderedDict()

        sum_fa_year = collections.OrderedDict()
        sum_f_year = collections.OrderedDict()
        sum_nr_year = collections.OrderedDict()
        sum_r_year = collections.OrderedDict()

        for x in units_list:
            fa_year_reg[x] = fa_year_r.filter(UnitName=x,).count()
            f_year_reg[x] = f_year_r.filter(UnitName=x,).count()
            nr_year_reg[x] = nr_year_r.filter(UnitName=x,).count()
            r_year_reg[x] = r_year_r.filter(UnitName=x,).count()
            fa_year_contr[x] = fa_year_c.filter(UnitName=x,).count()
            f_year_contr[x] = f_year_c.filter(UnitName=x,).count()
            nr_year_contr[x] = nr_year_c.filter(UnitName=x,).count()
            r_year_contr[x] = r_year_c.filter(UnitName=x,).count()

        sum_fa_year_reg = sum(fa_year_reg.values())
        sum_f_year_reg = sum(f_year_reg.values())
        sum_nr_year_reg = sum(nr_year_reg.values())
        sum_r_year_reg = sum(r_year_reg.values())
        sum_fa_year_c = sum(fa_year_contr.values())
        sum_f_year_c = sum(f_year_contr.values())
        sum_nr_year_c = sum(nr_year_contr.values())
        sum_r_year_c = sum(r_year_contr.values())

        for x in units_list:
            sum_fa_year[x] = fa_year_reg[x] + fa_year_contr[x]
            sum_f_year[x] = f_year_reg[x] + f_year_contr[x]
            sum_nr_year[x] = nr_year_reg[x] + nr_year_contr[x]
            sum_r_year[x] = r_year_reg[x] + r_year_contr[x]

        total_fa_year = sum(sum_fa_year.values())
        total_f_year = sum(sum_f_year.values())
        total_nr_year = sum(sum_nr_year.values())
        total_r_year = sum(sum_r_year.values())

        year_list = zip(
            units_list,
            f_year_reg.values(), f_year_contr.values(), sum_f_year.values(),
            r_year_reg.values(), r_year_contr.values(), sum_r_year.values(),
            nr_year_reg.values(), nr_year_contr.values(), sum_nr_year.values(),
            fa_year_reg.values(), fa_year_contr.values(), sum_fa_year.values(),
        )

        total_list = [
            sum_f_year_reg, sum_f_year_c, total_f_year,
            sum_r_year_reg, sum_r_year_c, total_r_year,
            sum_nr_year_reg, sum_nr_year_c, total_nr_year,
            sum_fa_year_reg, sum_fa_year_c, total_fa_year,
        ]

        context = {
            'list': year_list, 'total': total_list, 'year': GetYear,
        }

    return render(request, 'cy_detailed.html', context)


class ManhoursFilteredView(LoginRequiredMixin, TemplateView):
    template_name = 'manhours.html'
    login_url = '/users/login_user/'

    def get_queryset(self, **kwargs):
        return manhours.objects.all().order_by("unit_name")

    def get_context_data(self, **kwargs):
        context = super(ManhoursFilteredView, self).get_context_data(**kwargs)
        filter = ManhoursFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        table = ManhoursTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context
