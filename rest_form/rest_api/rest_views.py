from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_api.models import *
from rest_api.serializer import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from rest_api.decorators import *
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_api.form import password_validator,is_valid_email
from django.core.validators import validate_email
# Create your views here.


class register_page(ModelViewSet):
    serializer_class = RegisterSerializer

    def get_queryset(self, pk=None):
        if pk:
            data = User.objects.get(id=pk)
            return data
        else:
            data = User.objects.all()
            return data   

    def get(self,request,*args,**kwargs):
        datas = self.get_queryset()
        serializer = self.serializer_class(datas, many=True)
        data = serializer.data
        return Response(data)

    def retrieve(self,request,pk):
        if pk:
            datas = self.get_queryset(pk=pk)
            serializer = self.serializer_class(datas)
            data = serializer.data
            return Response(data)

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        data= request.data
        mail_error = is_valid_email(self.request.POST['email'])
        if mail_error:
            raise serializers.ValidationError('Invalid email address')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        elif User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already exists')
        else:
            password = data['password']
            print("len(password) ",len(password))
            error = password_validator(password)
            if error:
                raise serializers.ValidationError(error)
            user = User(
                    username = data['username'],
                    email= data['email'],
                )
            user.set_password(data['password'])
            user.save()
            return redirect('login_page')
            # elif serializer.is_valid():
            #     serializer.save()
            #     return redirect('login_page')
            # else:
            #     # print("else coming",serializer.errors)
            #     serializer = self.serializer_class(data=request.data)
        return Response({'messge':'Welcome','data':data,"errors":serializer.errors})
    
    def update(self,request,pk):
        if pk:
            data=self.get_queryset(pk=pk)
            serializer = self.serializer_class(instance=data,data=request.data)
            requested_data= request.data
            if User.objects.filter(email=requested_data['email']).exists():
                raise serializers.ValidationError('Email already exists please prefer other email')
            # elif User.objects.filter(username=requested_data['username']).exists():
            #     raise serializers.ValidationError('username already exists please prefer other username')
            else:    
                if serializer.is_valid():
                    serializer.save()
                    return redirect('register_list')
        return Response({'messge':'Welcome to update method','requested_data':requested_data,'data':data})
    
    def delete(self,request,pk):
        if pk:
            self.get_queryset(pk=pk).delete()
            return redirect('register_list')
        return Response({'messge':'Welcome to destory method'})

    # def get_data(self,request,pk):
    #     if pk:
    #         datas = self.get_queryset(pk=pk)
    #         serializer = self.serializer_class(datas)
    #         data = serializer.data
    #         return Response(data)

class Login_page(ModelViewSet):
    serializer_class = LoginSerializer
    
    def get_queryset(self, pk=None):
        if pk:
            data = User.objects.get(id=pk)
            return data
        else:
            data = User.objects.all()
            return data  

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        data= request.data
        # if not User.objects.filter(email=data['username'],password=data['password']).exists():
        #     raise serializers.ValidationError('Email or password are incorrect')
        # elif User.objects.filter(email=data['email'], password=data['password']).exists():
        #     return redirect('register_list')
        # else:
        #     serializer = self.serializer_class(data=request.data)
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Email or password are incorrect')
        else:
            login(request, user)
            return redirect('register_list')
        
        return Response({'messge':'Welcome to Login page','data':data})

    def logout_page(self,request,*args,**kwargs):
        logout(request)
        return redirect('login_page')
    
    
