from django import forms
from django.forms.widgets import DateInput



class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    second_name = forms.CharField(label='Second Name', max_length=100)
    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False)
    dob = forms.DateField(label='Date of Birth', widget=DateInput(attrs={'type': 'date'}))
    country = forms.ChoiceField(label='Country of Origin', choices=[('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda')])
