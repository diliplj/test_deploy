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
    

    #### create article ####
    path('article/', views.article.as_view(), name='article'),

    #### list article ###
    path('article_list/', views.article_list.as_view(), name='article_list'),

    #### delete article ###
    path('article_delete/<str:uid>/', views.article_list.as_view(), name='article_delete'),

    ### upload article ###
    path('article_upload/<str:uid>/', views.article_upload.as_view(), name='article_upload'),

    ### Home ####
    path('home/', views.Home.as_view(), name='home'),

]
