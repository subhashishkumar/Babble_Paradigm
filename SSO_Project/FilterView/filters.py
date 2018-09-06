import django_filters
from InputForms.models import *
from django_filters import STRICTNESS
from django_filters.widgets import RangeWidget


class AllAccdFilter(django_filters.FilterSet):
    Date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = AllAccident
        fields = ['Cause', 'EmpType', 'UnitName', 'Shift', 'Date', 'AccdType', 'Department', 'EmpName']

        strict = STRICTNESS.RETURN_NO_RESULTS
