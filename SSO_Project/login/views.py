# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# View for login
def login_user(request):
    next = request.GET.get('next', '/home')
    if request.method == "POST":
        username = request.POST.get('username',)
        password = request.POST.get('password',)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})

    return render(request, 'registration/login.html', {'redirect_to': next})


# View for Logout
def logged_out_user(request):
    logout(request)
    return render(request, 'welcome.html')


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    login_url = '/login_user/'
    success_url = reverse_lazy('password_updated')


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_updated.html'
    login_url = '/login_user/'
