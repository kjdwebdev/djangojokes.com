from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(message=f'{value} is in the past.', code='past_date')

EMPLOYTYPE = (
    (None, '--Please choose--'),
    ('ft', 'Full-time'),
    ('pt', 'Part-time'),
    ('ct', 'Contract work')
)

DAYS = (
    (1, 'MON'),
    (2, 'TUE'),
    (3, 'WED'),
    (4, 'THU'),
    (5, 'FRI')
)

class JobApplicationForm(forms.Form):
    YEARS = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False, 
            widget=forms.URLInput(
            attrs={'size': '50',
              'class': 'form-control',
              'placeholder': 'https://www.example.com',
              }
            ),
            validators=[URLValidator(schemes=['http', 'https'])]
    )
    employment_type = forms.ChoiceField(choices=EMPLOYTYPE, required=True)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(years=YEARS, 
          attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'}
        
        )
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS, 
        coerce=int,
        help_text='Select all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )
    hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'min': '10.00',
                'max': '100.00',
                'step': '.25'
            }
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )
    verify = forms.BooleanField(label='I certify that the information I have provided is true.')

