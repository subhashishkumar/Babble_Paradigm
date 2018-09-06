from InputForms.models import *
import django_tables2 as tables


class WithoutLPTable(tables.Table):
    class Meta:
        model = AllAccident
        # exclude = ('LearningPoint')
        sequence = (
            'AccdId', 'Date', 'UnitName', 'AccdType', 'EmpType', 'Cause', 'Department', 'Shift',
            'EmpID', 'EmpName', 'Narrative',
        )
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }


class WithLPTable(tables.Table):
    class Meta:
        model = AllAccident
        sequence = (
            'AccdId', 'Date', 'UnitName', 'AccdType', 'EmpType', 'Cause', 'Department', 'Shift',
            'EmpID', 'EmpName', 'Narrative', 'LearningPoint',
        )
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }


class ManhoursTable(tables.Table):
    RLTIFR = tables.Column('RLTIFR',)
    LTIFR = tables.Column('LTIFR', )
    SEVERITY_RATE = tables.Column('SEVERITY_RATE',)

    class Meta:
        model = manhours
        exclude = 'id'
        sequence = (
            'unit_name', 'date', 'manhours_worked_regular', 'manhours_worked_contract', 'mandays_lost',)
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }

