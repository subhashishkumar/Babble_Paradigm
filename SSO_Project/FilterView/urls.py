from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^AllFilterView/', views.AllFilteredView.as_view(), name='AllFilterView'),
    url(r'^get_unitname/', views.get_unitname, name='get_unitname'),
    url(r'^get_department/', views.get_department, name='get_department'),
]
