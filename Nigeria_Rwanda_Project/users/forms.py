from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    email = forms.CharField(label='Email', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    second_name = forms.CharField(label='Second Name', max_length=100)
    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False)
    dob = forms.DateField(label='Date of Birth', widget=DateInput(attrs={'type': 'date'}))
    country = forms.ChoiceField(label='Country of Origin', choices=[('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda')])
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'second_name', 'middle_name', 'dob', 'country', 'password']
        help_texts = {
            'username': None,
            'password': None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
