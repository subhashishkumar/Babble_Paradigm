from django.conf.urls import url

from homepage import views

urlpatterns = [
    url(r'^home$', views.HomePageView.as_view(), name='welcome'),
    url(r'^members/$', views.MemberPageView.as_view(), name='members'),
]
