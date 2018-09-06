# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html


# Register your models here.
def false(*args, **kwargs):
    """A simple no-op function to make our changes below readable."""
    return False


class abc(admin.ModelAdmin):
    list_display = ('created_at', 'emp_id', 'unit_name', 'emp_type', 'emp_name', 'age', 'dept', 'shift')


class xyz(admin.ModelAdmin):
    list_display = ('accd_id', 'accd_type', 'emp_id_link', 'date', 'cause', 'narrative', 'learning_point',)

    def emp_id_link(self, obj):
        url = reverse('admin:InputForms_emp_details_changelist',)
        return format_html("<a href='{}'>{}</a>", url, obj.emp_id)
    emp_id_link.admin_order_field = 'emp_id'
    emp_id_link.short_description = 'Employee ID'


class pqr(admin.ModelAdmin):
    list_display = (
        'AccdId', 'Date', 'UnitName', 'AccdType', 'Cause', 'EmpType', 'Department', 'Shift',
        'EmpID', 'EmpName', 'Narrative', 'LearningPoint',
    )

    actions = None
    has_add_permission = false
    has_delete_permission = false
    log_change = false
    message_user = false
    save_model = false


class ijk(admin.ModelAdmin):
    list_display = (
        'unit_name', 'date', 'manhours_worked_regular', 'manhours_worked_contract', 'mandays_lost',
        'RLTIFR', 'LTIFR', 'SEVERITY_RATE',
    )


admin.site.register(emp_details, abc)
admin.site.register(accd_details, xyz)
admin.site.register(AllAccident, pqr)
admin.site.register(manhours, ijk)
