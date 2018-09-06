from .models import *
from django import forms
from crispy_forms.layout import Field
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper, Layout


class EmpForm(ModelForm):
    class Meta:
        model = emp_details
        exclude = ["created_at", "id", "unit_name", ]


class AccdForm(ModelForm):
    class Meta:
        model = accd_details
        exclude = ["accd_id", "emp_id"]
        help_texts = {
            'date': ('Date Format : mm/dd/yyyy, Time Format : HH:MM'),
        }

    def clean(self):
        cleaned_data = super(AccdForm, self).clean()
        accd_type = self.cleaned_data.get("accd_type")
        if accd_type == 'Fatal':
            LP = self.cleaned_data.get("learning_point")
            if LP == '':
                msg = forms.ValidationError("This field is required.")
                self.add_error('learning_point', msg)
        else:
            self.cleaned_data['learning_point'] = '----'
        return self.cleaned_data


class ManhoursForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('date', id="manhours_date"),
            Field('manhours_worked_regular',),
            Field('manhours_worked_contract',),
            Field('mandays_lost',),
        )
        super(ManhoursForm, self).__init__(*args, **kwargs)

    class Meta:
        model = manhours
        exclude = ["unit_name", ]
