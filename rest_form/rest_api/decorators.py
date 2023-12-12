from rest_api.models import *
from django.shortcuts import render, redirect
from rest_api.models import *
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages

def admin_only(function):
    def wrapper(request, *args, **kwargs):
        try:
            user_data=User.objects.get(username=request.session.get('username'),email=request.session.get('email'))
            if user_data.email:# and request.user.is_authenticated:
                if Role.objects.filter(email__email=user_data.email, role="admin").exists():
                    return function(request, *args, **kwargs)
                else:
                    messages.warning('You are not an admin')
                    return redirect('login') 
            else:
                messages.warning('You are not logged in')
                return function(request, *args, **kwargs)
            
        except Exception as e:
            print("eeee ",e)
            return HttpResponse(e)
    
    return wrapper