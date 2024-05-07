from typing import Self
from django import forms
from django.forms import ValidationError

from .models import User


# Create your forms here.
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']

    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs) -> None:
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    

    def clean_password_confirm(self: Self) -> forms.CharField:
        cd: dict = self.cleaned_data

        if cd['password'] == cd['password_confirm']:
            return cd['password']
        
        raise ValidationError('Las contraseñas no coinciden. :(')
    

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def __init__(self: Self, *args, **kwargs) -> None:
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'example@gmail.com'

        #self.fields['email'].widget.attrs['aria-describedby'] = self.fields['email'].id
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
