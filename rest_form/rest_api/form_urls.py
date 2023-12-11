from django.urls import path, include
from rest_api import form_views as views

urlpatterns = [
    #### REGISTER ######
    path('list/',views.user_list_page.as_view(),name='list'),
    #delete
    path('delete/<int:pk>/',views.user_list_page.as_view(),name='delete'),
    #create
    path('register/',views.user_create.as_view(),name='register'),
    #update
    path('update/<int:pk>/',views.user_update.as_view(),name='update'),

    #### LOGIN ######
    path('login/',views.user_login.as_view(),name='login'),

]
