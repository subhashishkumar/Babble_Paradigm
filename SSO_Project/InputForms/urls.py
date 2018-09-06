
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^empform/$', views.EmpView.as_view(), name='EmpView'),
    url(r'^accdform/$', views.AccdView.as_view(), name='AccdView'),
    url(r'^manhoursform/$', views.ManhoursView.as_view(), name='ManhoursView'),
]
