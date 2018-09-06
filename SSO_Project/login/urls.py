from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logged_out_user, name='logged_out_user'),
    url(r'^password_change/$', views.CustomPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change_done/$', views.CustomPasswordChangeDoneView.as_view(), name='password_updated'),
]
