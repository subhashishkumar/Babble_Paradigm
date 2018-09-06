import django_filters
from InputForms.models import *
from django_filters import STRICTNESS
from django_filters.widgets import RangeWidget


class ManhoursFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = manhours
        fields = ['date', 'unit_name']

        strict = STRICTNESS.RETURN_NO_RESULTS
