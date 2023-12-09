from typing import Any
from .models import *
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'username' ,'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)   
        print("instance",instance) 

class EditRegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'username' ,'password']

    def __init__(self, *args, **kwargs):
        super(EditRegisterForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)   
        print("instance",self.instance)         

