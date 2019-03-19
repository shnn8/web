from django import forms
from main.models import UserProfileInfo
from django.contrib.auth.models import User
from django.conf import settings
class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta():
    model = User
    fields = ('username','password','first_name','last_name','email',)
class UserProfileInfoForm(forms.ModelForm):
 
 class Meta():
    model = UserProfileInfo
    fields = ('portfolio_site','birth_date')
    birth_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)