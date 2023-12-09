from django.urls import path, include
from .form_views import *
from . import rest_views

urlpatterns = [
    path('register_create/',rest_views.register_page.as_view({'post':'create'}), name="register_create"),
    path('register_list/',rest_views.register_page.as_view({'get':'get'}), name="register_list"),
    # path('get_data/<int:pk>/',rest_views.register_page.as_view({'get':'get_data'}), name="get_data"),
    path('register_update/<int:pk>/',rest_views.register_page.as_view({'post':'update'}),name="register_update"),
    path('register_retrieve/<int:pk>/',rest_views.register_page.as_view({'get':'retrieve'}),name="register_retrieve"),
    path('register_delete/<int:pk>/',rest_views.register_page.as_view({'get':'delete'}),name="register_delete"),
]
