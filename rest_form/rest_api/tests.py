from django.test import TestCase

# Register.objects.filter(id=id).update(
# 						email=request.POST.get('email'),
# 						username= request.POST.get('username'),
# 						password=request.POST.get('password'))


# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=dilip
# Group=dilip
# WorkingDirectory=/home/dilip/Documents/deployment/test_deploy/rest_form
# ExecStart=/home/dilip/Documents/deployment/test_deploy/rest_form/prod1/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock rest_form.wsgi:application

# [Install]
# Restart=always
# 


# working
# gunicorn --bind 127.0.0.1:8002 --workers=3 rest_form.wsgi:application


#### Nginx #####

# server {
#     listen 80;
#     server_name 127.0.0.1;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /home/dilip/Documents/deployment/test_deploy/rest_form;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }


# {% for message in messages %}
#     <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
#     {% endfor %}


'''

# assuming which duplicate is removed doesn't matter...
for row in MyModel.objects.all().reverse():
    if MyModel.objects.filter(photo_id=row.photo_id).count() > 1:
        row.delete()

'''

'''

{% include 'head.html' %}
{% block content %}
    <div class="container-fluid d-flex justify-content-md-center ">
        
        <form action="{% url 'register' %}" method="post">
            {% csrf_token %}
          
            <div class="panel-heading"><h4 style="text-align: center;">Register</h4></div>
              <div class="form-group" >
                  <label for="exampleInputPassword1">Username</label>
                  <div class="col-md-6">
                      {{ form.username }}
                  </div>
                  {% if messages %}
                  {% for msg in messages %}
                  <small id="emailHelp" class="text-danger">{{msg}}</small>
                  {% endfor %}
                  {% else %}
                  <small id="emailHelp" class="text-danger">{{ form.errors.username }}</small>
                  {% endif %}
                </div>
              
              <div class="form-group">
                <label for="exampleInputEmail1">Email address</label>
                <div class="col-md-6">
                  {{ form.email }}
                  </div>
                <small id="emailHelp" class="text-danger">{{ form.errors.email }}</small>
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                  <div class="col-md-6">
                      {{ form.password }}
                  </div>
                  <small id="emailHelp" class="text-danger">{{ form.errors.password }}</small>
              </div>
              <div class="col-auto my-2">
              <button type="submit" class="btn btn-primary">Submit</button>
                  </div>
                              
                <div class="">
                  <small class="alert-heading text-dark">Note!</small>
                  <ul>
                    <li class="text-danger" style="font-size: x-small;">The password must contain lowercase character.</li>
                    <li class="text-danger" style="font-size: x-small;">The password must contain uppercase character.</li>
                    <li class="text-danger" style="font-size: x-small;">The password must contain numbers.</li>
                    <li class="text-danger" style="font-size: x-small;"> length should be atleast 8.</li>
                    </ul>
                  
                </div>   

              <div class="col-auto my-2">
                <small id="emailHelp" class="text-dark">if you have an account please </small>
                <a href="{% url 'login' %}" class="text-primary" style="text-decoration:none">Login</a>
                    </div>    
                   
                  </form>

    </div>
{% endblock %}

'''
'''
<div class="form-group my-3">
            <label for="exampleInputUsername1">Title</label>
            <div class="col-md-6">
            {{ form.title }}
            </div>
            <small id="emailHelp" class="text-danger">{{ form.errors.title }}</small>
            
        </div>
        <div class="form-group my-3">
            <label for="exampleInputPassword1">Headline</label>
            <div class="col-md-6 input-group-lg">
                {{ form.headline }}
            </div>
            <small id="emailHelp" class="text-danger">{{ form.errors.headline }}</small>
        </div>
        
        <div class="form-group col-md-6 my-3">
            <label for="exampleFormControlTextarea1" class="form-label">Content</label>
                {{form.body}}
        </div>
        
        <div class="col-md-3">
            <label for="formFile" class="form-label">{{ form.image.label }}</label>
            <!-- <input class="form-control" type="file" id="formFile"> -->
            {{ form.image }}
        </div>
        
        <div class="col-auto my-2">
        <button type="submit" class="btn btn-primary">Add blog</button>
            </div>
            
        <!-- <div class="col-auto my-2">
        <small id="emailHelp" class="text-dark">if you don't have an account please </small>
        <a href="{% url 'register' %}" class="text-primary" style="text-decoration:none">Register</a>
            </div>      -->


'''

'''

<div class="container-fluid d-flex justify-content-md-center align-items-center">
    <form action="{% url 'otp' %}" method="post">
        {% csrf_token %}
        <div class="panel-heading "><h6>We have sent OTP to your email 
            {% if email %} {{ email }}{% endif %}
            please check it</h6></div>
        <div class="form-group">
            <label for="exampleInputUsername1">OTP</label>
            <div class="col-md-6">
            {{ form.otp }}
            </div>
            {% for msg in messages %}
                {% if msg %}
                    <small id="emailHelp" class="text-danger"> {{msg}}</small>
                {% else %}
                    <small id="emailHelp" class="text-danger">  {{ form.errors.otp }}</small>
                    {% endif %}
            {% endfor %}
        </div>
        
        <div class="col-auto my-2">
        <button type="submit" class="btn btn-primary">Enter</button>
            </div>
            
        <div class="col-auto my-2">
        <small id="emailHelp" class="text-dark"> If you didnt receive OTP Yet</small>
        <a href="{% url 'otp' 'resend' %}" class="text-primary" style="text-decoration:none">Resend again</a>
            </div>     
      </form>

</div>      



'''