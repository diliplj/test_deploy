from django.urls import path, include, reverse_lazy
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

    ### LOGOUT ####
    path('logout/', views.user_logout.as_view(), name='logout'),

    ### OTP ###
    path('otp/', views.OTP_Page.as_view(), name='otp'),

    ### resend OTP ###
    path('otp/<str:resend>/', views.OTP_Page.as_view(), name='otp'),
    

    #### create blog ####
    path('blog/', views.blog.as_view(), name='blog'),

    #### list blog ###
    path('blog_list/', views.blog_list.as_view(), name='blog_list'),

    #### delete blog ###
    path('blog_delete/<str:uid>/', views.blog_list.as_view(), name='blog_delete'),

    ### upload blog ###
    path('blog_upload/<str:uid>/', views.blog_upload.as_view(), name='blog_upload'),

    ### Home ####
    path('blog_detail_page/<str:uid>/', views.blog_detail_page.as_view(), name='blog_detail_page'),

]
