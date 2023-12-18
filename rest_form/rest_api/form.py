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
	
	if int(len(password)) > 8:
		err="Password length should be atleast 8 "
	return err

def is_valid_email(email):
    error = ""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{3,3}$'
    if not re.match(pattern, email):
        error = "Invalid email address"
        return error

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username' ,'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)   

    def clean_email(self):
        data = self.cleaned_data.get('email')
        mail_error = is_valid_email(data)
        if mail_error:
            raise forms.ValidationError(mail_error)

        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(("This email is already exists"))
        return data
    
    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if User.objects.filter(username=username).exists():
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
        model = User
        fields = ['email', 'username']

    def __init__(self, *args, **kwargs):
        super(EditRegisterForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)   
        print("instance",self.instance)         

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     err = password_validator(password)
    #     if err:	
    #         raise forms.ValidationError((err))
    #     return password

    def clean_email(self):
        data = self.cleaned_data.get('email')
        
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(("This email is already exists please prefer other email"))
        return data
    
    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(("This username is already exists please prefer other username"))
        return username

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=255)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)   
      
    def clean_username(self):
        data = self.cleaned_data.get('username')
        if not User.objects.filter(username=data).exists():
            print("form username error ")
            raise forms.ValidationError(("This username is not exists"))
        return data
    
    def clean_password(self):  
        password = self.cleaned_data.get('password')
        data = self.cleaned_data.get('username')  
        if not User.objects.filter(username=data,password=password).exists():
            print("form password error ")
            raise forms.ValidationError(("Password is incorrect"))
        return password
    

class OTPForm(forms.ModelForm):
    # otp = forms.CharField( widget=forms.TextInput(attrs={'type':'number','max':6}))
    class Meta:
        model = OTP
        fields = ['otp']
    
    def __init__(self,*args, **kwargs):
        super(OTPForm, self).__init__(*args, **kwargs)

    def clean_otp(self):
        otp_data = self.cleaned_data.get('otp')
        if otp_data in [None,''] and type(otp_data) == str:
            raise forms.ValidationError(('Enter Valid 6 digits OTP number'))      


class ArticleForm(forms.ModelForm):
    image = forms.ImageField(label="Article Image")
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        # self.instance = getattr(self, 'instance', None)
        self.fields['title'].widget.attrs['size'] = 50
        self.fields['headline'].widget.attrs['size'] = 50
        self.fields['headline'].widget.attrs['style']  = 'width:500px; height:80px;'
    
    class Meta:
        model = Article
        fields = ['title','headline','body','image']

class UploadArticleForm(forms.ModelForm):     
    image = forms.ImageField(label="Article Image")
    
    def __init__(self, *args, **kwargs):
        super(UploadArticleForm, self).__init__(*args, **kwargs)
        # self.instance = getattr(self, 'instance', None)
        self.fields['title'].widget.attrs['size'] = 50
        self.fields['headline'].widget.attrs['size'] = 50
        self.fields['headline'].widget.attrs['style']  = 'width:500px; height:80px;'
    
    class Meta:
        model = Article
        fields = ['title','headline','body','image']