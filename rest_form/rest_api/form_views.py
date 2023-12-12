from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse,response,HttpResponse
from rest_api.form import *
from rest_api.decorators import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@method_decorator(admin_only, name='dispatch')
class user_list_page(TemplateView):
    
    msg = ""
    def get(self,request,*args,**kwargs):
        #listing the user
        if not kwargs.get('pk'):
            template_name = 'user_list.html'
            data = Register.objects.all()
            form = RegisterForm()
            msg="Success"
            return render(request,template_name,{'form':form,'datas':data})
        
        # deleting user
        else:
            id = kwargs.get('pk')
            if Register.objects.filter(pk=id).exists():
                Register.objects.filter(pk=id).delete()
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
            if User.objects.filter(username=self.request.POST['username']).exists():
                messages.success(request,"The username is already exist!")
            else:
                if form.is_valid():
                    user = User(
                        username = self.request.POST['username'],
                        email = self.request.POST['email'],
                        is_active = True,
                        is_staff = False
                    )
                    user.set_password(self.request.POST['password'])
                    user.save()
                    form.save()
                    self.request.session['username'] = self.request.POST['username']
                    self.request.session['email'] = self.request.POST['email']
                    msg = "Success"
                    return redirect('list')
                else:
                    form = RegisterForm(self.request.POST)
                    print(form.errors.as_data)
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
            email = self.request.POST['email']
            password = self.request.POST['password']
            if Register.objects.filter(email=email, password=password).exists():
                self.request.session['email'] = self.request.POST['email']
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
            data = Register.objects.get(pk=id)
            form = EditRegisterForm(instance=data)
            return render(request,self.template_name,{'form':form, 'data':data,"id":id})
        else:
            return render(request,self.template_name,{'form':form})

    def post(self,request,pk,*args,**kwargs):
        print("post comming",pk)
        form = EditRegisterForm()
        if self.request.method == "POST":
            dataaa = Register.objects.filter(pk=pk)
                
            Register.objects.filter(pk=pk).update(
                username=self.request.POST['username'],email=self.request.POST['email'],
                password=self.request.POST['password']
            )
            self.request.session['username'] = self.request.POST['username']
            self.request.session['email'] = self.request.POST['email']
            return redirect('list')
        return render(request,self.template_name,{'form':form,"id":pk})
