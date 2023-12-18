from rest_api.models import *
from django.shortcuts import render, redirect
from rest_api.models import *
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages

def admin_only(function):
    def wrapper(request, *args, **kwargs):
        try:
            print("request.user ",request.user)
            if str(request.user) not in ['AnonymousUser', None]:  
                print(" coming inside ")
                user_data=User.objects.get(username=request.user)
                if user_data.username:# and request.user.is_authenticated:
                    if Role.objects.filter(email__email=user_data.email, role="admin").exists():
                        return function(request, *args, **kwargs)
                    else:
                        print("you are not admin")
                        messages.warning(request,'You are not an admin')
                        return redirect('login') 
                else:
                    # messages.warning(request,'You are not logged in')
                    return redirect('login')
            else:
                return redirect('login')    
        except Exception as e:
            return HttpResponse(e)
    
    return wrapper