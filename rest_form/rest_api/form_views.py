from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse,response,HttpResponse
from rest_api.form import *

class user_list_page(TemplateView):
    
    msg = ""
    def get(self,request,*args,**kwargs):
        #listing the user
        if not kwargs.get('pk'):
            template_name = 'user_list.html'
            data = Register.objects.all()
            form = RegisterForm()
            return render(request,template_name,{'form':form,'datas':data})
        
        # deleting user
        else:
            id = kwargs.get('pk')
            if Register.objects.filter(pk=id).exists():
                Register.objects.filter(pk=id).delete()
                return redirect('list')
            

class user_create(TemplateView):
    template_name = "register.html"
    
    def get(self,request,*args,**kwargs):
        form = RegisterForm()
        if kwargs.get('pk'):
            id = kwargs.get('pk')
            data = Register.objects.get(pk=id)
            form = RegisterForm(self.request.POST)
            
            return render(request,self.template_name,{'form':form, 'data':data})
        else:
            return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = RegisterForm()
        if self.request.method == "POST":
            form = RegisterForm(self.request.POST)
            if form.is_valid():
                form.save()
                msg = "Success"
                return redirect('list')
            else:
                error = form.errors.as_data()
            return render(request,self.template_name,{'form':form})

class user_update(TemplateView):
    template_name = "update_register.html"
    
    def get(self,request,*args,**kwargs):
        form = RegisterForm()
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
            return redirect('list')
        return render(request,self.template_name,{'form':form,"id":pk})
