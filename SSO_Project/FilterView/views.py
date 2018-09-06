# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from .filters import *
from InputForms.models import *
from login.models import *
from OutputViews.tables import *
from django_tables2 import RequestConfig
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AllFilteredView(LoginRequiredMixin, TemplateView):
    template_name = 'filter_view.html'
    login_url = '/users/login_user/'

    def get_queryset(self, **kwargs):
        return AllAccident.objects.all().defer("LearningPoint").order_by("-AccdId")

    def get_context_data(self, **kwargs):
        context = super(AllFilteredView, self).get_context_data(**kwargs)
        filter = AllAccdFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        table = WithoutLPTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


def get_unitname(request):
    if request.is_ajax():
        unit_get = request.GET.get('term', '')
        unitres = profile.objects.filter(unit__icontains=unit_get)

        unit_results = []

        for x in unitres:
            units_json = {}
            units_json['label'] = x.unit
            units_json['value'] = x.unit

            if units_json not in unit_results:
                unit_results.append(units_json)

        data = json.dumps(unit_results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_department(request):
    if request.is_ajax():
        dept_get = request.GET.get('term', '')
        deptres = AllAccident.objects.filter(Department__icontains=dept_get)

        dept_results = []

        for x in deptres:
            dept_json = {}
            dept_json['label'] = x.Department
            dept_json['value'] = x.Department

            if dept_json not in dept_results:
                dept_results.append(dept_json)

        data = json.dumps(dept_results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
