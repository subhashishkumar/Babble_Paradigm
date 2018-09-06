from AccdStats import views
from django.conf.urls import url

urlpatterns = [
    url(r'^summary', views.summary, name='Summary'),
]
