# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import *
from login.models import *
from InputForms.models import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def getUnitName(self):
    if self.request.user.is_authenticated():
        current_user = self.request.user.username
        uname = User.objects.get(username=current_user)
        unit = uname.profile.unit
        return unit


class EmpView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = emp_details
    form_class = EmpForm
    login_url = '/users/login_user/'
    success_url = reverse_lazy('AccdView')
    success_message = 'Success! Employee Data Submitted'

    def form_valid(self, form):
        emp_details = form.save(commit=False)
        emp_details.unit_name = getUnitName(self)
        emp_details.save()
        return SuccessMessageMixin.form_valid(self, form)


class AccdView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = accd_details
    form_class = AccdForm
    login_url = '/users/login_user/'
    success_url = reverse_lazy('EmpView')
    success_message = 'Success! Accident Data Submitted'

    def form_valid(self, form):
        accd_details = form.save(commit=False)
        unit = getUnitName(self)
        accd_details.emp_id = emp_details.objects.filter(unit_name=unit,).latest('created_at')
        accd_details.save()
        return SuccessMessageMixin.form_valid(self, form)


class ManhoursView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = manhours
    form_class = ManhoursForm
    login_url = '/users/login_user/'
    success_url = reverse_lazy('ManhoursView')
    success_message = 'Success! Data Submitted'

    def form_valid(self, form):
        manhours = form.save(commit=False)
        manhours.unit_name = getUnitName(self)
        manhours.save()
        return SuccessMessageMixin.form_valid(self, form)
