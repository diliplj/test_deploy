from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_api.models import *
from rest_api.serializer import *
from django.shortcuts import render,redirect
# Create your views here.


class register_page(ModelViewSet):
    serializer_class = RegisterSerializer

    def get_queryset(self, pk=None):
        if pk:
            data = Register.objects.get(id=pk)
            return data
        else:
            data = Register.objects.all()
            return data   

    def get(self,request,*args,**kwargs):
        datas = self.get_queryset()
        serializer = self.serializer_class(datas, many=True)
        data = serializer.data
        return Response(data)

    def retrieve(self, request,pk):
        if pk:
            datas = self.get_queryset(pk=pk)
            serializer = self.serializer_class(datas)
            data = serializer.data
            return Response(data)

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        data= request.data
        if Register.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        elif Register.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already exists')
        else:
            if serializer.is_valid():
                serializer.save()
                return redirect('register_list')
            else:
                serializer = self.serializer_class(data=request.data)
        return Response({'messge':'Welcome to post method','data':data})
    
    def update(self,request,pk):
        if pk:
            data=self.get_queryset(pk=pk)
            serializer = self.serializer_class(instance=data,data=request.data)
            requested_data= request.data
            if Register.objects.filter(email=requested_data['email']).exists():
                raise serializers.ValidationError('Email already exists please prefer other email')
            # elif Register.objects.filter(username=requested_data['username']).exists():
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
            data = Register.objects.get(id=pk)
            return data
        else:
            data = Register.objects.all()
            return data  
        
    # def get(self,request,*args,**kwargs):
    #     datas = self.get_queryset()
    #     serializer = self.serializer_class()
    #     print("is get is calling? ")
    #     return Response({'messge':'Welcome to Login page'})


    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        data= request.data
        if not Register.objects.filter(email=data['email'],password=data['password']).exists():
            raise serializers.ValidationError('Email or password are incorrect')
        elif Register.objects.filter(email=data['email'], password=data['password']).exists():
            return redirect('register_list')
        else:
            serializer = self.serializer_class(data=request.data)
        return Response({'messge':'Welcome to Login page','data':data})


    
    
