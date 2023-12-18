from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse,response,HttpResponse
from rest_api.form import *
from rest_api.decorators import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from rest_api.api import six_digit_otp ,send_otp_to_email
from django.core.exceptions import ValidationError

@method_decorator(admin_only, name='dispatch')
class user_list_page(TemplateView):
    
    msg = ""
    def get(self,request,*args,**kwargs):
        #listing the user
        if not kwargs.get('pk'):
            template_name = 'user_list.html'
            data = User.objects.all()
            form = RegisterForm()
            msg="Success"
            return render(request,template_name,{'form':form,'datas':data,"messages":msg})
        
        # deleting user
        else:
            id = kwargs.get('pk')
            if User.objects.filter(pk=id).exists():
                User.objects.filter(pk=id).delete()
                return redirect('list')

        return HttpResponse(msg)    

class user_create(TemplateView):
    template_name = "register.html"
    
    def get(self,request,*args,**kwargs):
        form = RegisterForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = RegisterForm()
        if self.request.method == "POST":
            form = RegisterForm(self.request.POST)
            if form.is_valid():
                user = User(
                    username = self.request.POST['username'],
                    email= self.request.POST['email'],
                )
                user.set_password(self.request.POST['password'])
                user.save()
                # form.save()
                msg = "Success"
                digit,email = six_digit_otp(6,self.request.POST['email'])
                OTP.objects.create(email = email, otp=digit)
                msg = send_otp_to_email(digit,email)
                if msg:
                    self.request.session['verify_email'] = email
                uid_field = UserTable()
                uid_field.user = user
                uid_field.save()

                return redirect('otp')
            else:
                form = RegisterForm(self.request.POST)
                email = self.request.POST['email']
        return render(request,self.template_name,{'form':form,'msg':messages})

class user_login(TemplateView):
    template_name = "login.html"
    
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = LoginForm()
        if self.request.method == "POST":
            form = LoginForm(self.request.POST)
            username = self.request.POST['username']
            password = self.request.POST['password']
            print("username ",username,"password ",password)
            user = authenticate(username=username, password=password)
            if user is None:
                print("form errors ", form.errors)
                print("user ",user)
            else:
                login(request, user)
                return redirect('list')
            
        else:
            form = LoginForm(self.request.POST)
        return render(request,self.template_name,{'form':form})


class user_update(TemplateView):
    template_name = "update_register.html"
    
    def get(self,request,*args,**kwargs):
        form = EditRegisterForm()
        if kwargs.get('pk'):
            id = kwargs.get('pk')
            data = User.objects.get(pk=id)
            form = EditRegisterForm(instance=data)
            return render(request,self.template_name,{'form':form, 'data':data,"id":id})
        else:
            return render(request,self.template_name,{'form':form})

    def post(self,request,pk,*args,**kwargs):
        form = EditRegisterForm()
        if self.request.method == "POST":
            dataaa = User.objects.get(pk=pk)
            User.objects.filter(pk=pk).update(
                username=self.request.POST['username'],email=self.request.POST['email']
            )    
            user = User.objects.get(email=self.request.POST['email'])
            # user.set_password(self.request.POST['password'])
            user.save()
            return redirect('list')
        return render(request,self.template_name,{'form':form,"id":pk})

class user_logout(TemplateView):
    template_name = "login.html"
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('login')


class OTP_Page(TemplateView):
    template_name = "otp.html"
    
    def get(self,request,*args,**kwargs):
        form = OTPForm()
        if kwargs.get('resend'):
            print("self.request.session.get('verify_email')",self.request.session.get('verify_email'))
            digit,email = six_digit_otp(6,self.request.session.get('verify_email'))
            OTP.objects.filter(email = email).update(otp=digit)
            msg = send_otp_to_email(digit,email)
        
        return render(request,self.template_name,{'form':form,"email":self.request.session.get('verify_email')})

    def post(self,request,*args,**kwargs):
        form = OTPForm()
        otp_data = self.request.POST['otp']
        form = OTPForm(self.request.POST)
        email = self.request.session.get('verify_email')
        if self.request.method == "POST":
            if OTP.objects.filter(otp=otp_data, email=email).exists():
                OTP.objects.filter(otp=otp_data, email=email).update(
                    is_verified = True
                )
                del self.request.session['verify_email']
                return redirect('login')
            else:
                messages.warning(request,'Invalid OTP')
        else:
            form = OTPForm(self.request.POST)
        return render(request,self.template_name,{'form':form})  


@method_decorator(admin_only, name='dispatch')
class article_list(TemplateView):
    template_name = 'article_list.html'
    def get(self,request,*args,**kwargs):
        if not kwargs.get('uid'):
            article_data= Article.objects.all()
            return render(request,self.template_name,{'article_datas':article_data})
        else:
            uid = kwargs.get('uid')
            if Article.objects.filter(uid=uid).exists():
                Article.objects.filter(uid=uid).delete()
                return redirect('article_list')



@method_decorator(admin_only, name='dispatch')
class article(TemplateView):
    template_name = "article.html"
    
    def get(self,request,*args,**kwargs):
        form = ArticleForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = ArticleForm()
        if request.method =="POST":
            form = ArticleForm(request.POST,request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.created_by = request.user.email if request.user.email else request.user
                article.updated_by = request.user.email if request.user.email else request.user
                article.save()
                return redirect('article_list')
            else:
                print(form.error)
                form = ArticleForm(request.POST,request.FILES)
        return render(request,self.template_name,{'form':form})        

@method_decorator(admin_only, name='dispatch')
class article_upload(TemplateView):
    template_name = "article_upload.html"
    
    def get(self,request,*args,**kwargs):
        form = UploadArticleForm()
        if kwargs.get('uid'):
            uid =kwargs.get('uid')
            if Article.objects.filter(uid=uid).exists():
                data = Article.objects.get(uid=uid)
                print(" get is working")
                form = UploadArticleForm(instance=data)
                return render(request,self.template_name,{'form':form, 'data':data,"uid":uid})

        return render(request, self.template_name,{'form':form})

    def post(self,request,uid,*args,**kwargs):
        form = UploadArticleForm()
        data = Article.objects.get(uid=uid)
        if request.method =="POST":
            form = UploadArticleForm(request.POST,request.FILES, instance=data)
            if form.is_valid():
                article_upload = form.save(commit=False)
                article_upload.created_by = request.user.email if request.user.email else request.user
                article_upload.updated_by = request.user.email if request.user.email else request.user
                article_upload.save()
                return redirect('article_list')
            else:
                print(form.error)
                form = UploadArticleForm(request.POST,request.FILES)
        return render(request,self.template_name,{'form':form,"data":data,"uid":uid})        

class Home(TemplateView):
    def get(self,request,*args,**kwargs):
        articles=  Article.objects.all()

    # def post(self,request,*args,**kwargs):
    #     pass