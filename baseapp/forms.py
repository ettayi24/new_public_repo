from django import forms
from django.core import validators
from .models import *

validators.MaxLengthValidator


# def max_len(value):
#     if len(value)>2:
#         raise ValidationError("max len exceeded")

def check_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError('need to start with z')


class FormName(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(3)])
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("gotcha bot!")
    #     return botcatcher
    
#modelforms
class UserForm(forms.ModelForm):

    
    class Meta:
        model = User
        fields = "__all__"


class AdminUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=adminUser
        fields=('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio','profile_pic')