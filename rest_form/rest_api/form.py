from .models import *
from django import forms
from django.db.models import Q
import re


def password_validator(password):
	err = ''
	if re.search('[a-z]', password) is None:
		err='The password must contain one lowercase character.'
		
	if re.search('[A-Z]', password) is None:
		err='The password must contain one uppercase character.'
	
	if re.search('[0-9]', password) is None:
		err='The password must contain numbers .'
	
	if len(password) <5:
		err="Password length should be atleast 5 "
	return err


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'username' ,'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)   

    def clean_email(self):
        data = self.cleaned_data.get('email')
        
        if Register.objects.filter(email=data).exists():
            raise forms.ValidationError(("This email is already exists"))
        return data
    
    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if Register.objects.filter(username=username).exists():
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(("This username is already exists"))
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        err = password_validator(password)
        if err:	
            raise forms.ValidationError((err))
        return password
    
        
class EditRegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'username' ,'password']

    def __init__(self, *args, **kwargs):
        super(EditRegisterForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)   
        print("instance",self.instance)         

    def clean_password(self):
        password = self.cleaned_data.get('password')
        err = password_validator(password)
        if err:	
            raise forms.ValidationError((err))
        return password

    def clean_email(self):
        data = self.cleaned_data.get('email')
        
        if Register.objects.filter(email=data).exists():
            raise forms.ValidationError(("This email is already exists please prefer other email"))
        return data
    
    # def clean_username(self):  
    #     username = self.cleaned_data.get('username')  
    #     if Register.objects.filter(username=username).exists():
    #         raise forms.ValidationError(("This username is already exists please prefer other username"))
    #     return username

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=255)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)   
      
    def clean_email(self):
        data = self.cleaned_data.get('email')
        if not Register.objects.filter(email=data).exists():
            print("form email error ")
            raise forms.ValidationError(("This email is not exists"))
        return data
    
    def clean_password(self):  
        password = self.cleaned_data.get('password')
        data = self.cleaned_data.get('email')  
        if not Register.objects.filter(email=data,password=password).exists():
            print("form password error ")
            raise forms.ValidationError(("Password is incorrect"))
        return password
    

    
