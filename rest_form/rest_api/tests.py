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