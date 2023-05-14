from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class SignUpForm(forms.ModelForm):
#     email = forms.CharField(label='Email', max_length=100)
#     first_name = forms.CharField(label='First Name', max_length=100)
#     second_name = forms.CharField(label='Second Name', max_length=100)
#     middle_name = forms.CharField(label='Middle Name (if any)', max_length=100, required=False)
#     dob = forms.DateField(label='Date of Birth', widget=DateInput(attrs={'type': 'date'}))
#     country = forms.ChoiceField(label='Country of Origin', choices=[('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda')])
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'second_name', 'middle_name', 'dob', 'country', 'password']
        
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
    
# def clean_username(self):
#         username = self.cleaned_data.get('username')
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError('This username is already taken.')
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    dob = forms.DateField(label='Date of Birth', widget=DateInput(attrs={'type': 'date'}))
    country = forms.ChoiceField(label='Country of Origin', choices=[('Nigeria', 'Nigeria'), ('Rwanda', 'Rwanda')])
    first_name = forms.CharField(label='First Name', max_length=100)
    second_name = forms.CharField(label='Second Name', max_length=100)
    middle_name = forms.CharField(label='Middle Name (if any)', max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'second_name', 'middle_name', 'email', 'password1', 'password2', 'country', )
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already taken.')