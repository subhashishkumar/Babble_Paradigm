from OutputViews import views
from django.conf.urls import url


urlpatterns = [
    url(r'^showtables/home$', views.showtables, name='ShowTables'),
    url(r'^showtables/accdtype/(?P<accdType>\D+)/$', views.get_data_view, name='FatalDataView'),
    url(r'^showtables/accdtype/(?P<accdType>\D+)/$', views.get_data_view, name='FirstAidDataView'),
    url(r'^showtables/accdtype/(?P<accdType>\D+)/$', views.get_data_view, name='ReportableDataView'),
    url(r'^showtables/accdtype/(?P<accdType>\D+)/$', views.get_data_view, name='NonReportableDataView'),
    url(r'^showtables/yearly_detailed/$', views.year_wise_detailed, name='cy_detailed'),
    url(r'^showtables/manhours/$', views.ManhoursFilteredView.as_view(), name='ManhoursTableView'),
]
