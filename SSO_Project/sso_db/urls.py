"""sso_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.admin import AdminSite
from django.contrib import admin

admin.site.site_header = ('SSO Administration')
admin.site.index_title = ('SSO Administration')
admin.site.site_title = ('SSO Administration')

AdminSite.login_template = 'registration/admin_login.html'
AdminSite.logout_template = 'registration/logout.html'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
    url(r'^users/', include('login.urls')),
    url(r'^forms/', include('InputForms.urls')),
    url(r'^output/', include('OutputViews.urls')),
    url(r'^filter/', include('FilterView.urls')),
    url(r'^stats/', include('AccdStats.urls')),
]
