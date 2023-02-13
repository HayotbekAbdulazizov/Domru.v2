from os import name
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter   # REST-Framework


app_name = 'api'


urlpatterns = [
# API view
    path('post/', views.PostApiView.as_view(), name='postCreateView'),
    path('post/contact/', views.PostContactApiView.as_view(), name='postContactCreateView'),
    path('post/contact2/', views.PostContactGetView.as_view(), name='postContactGetView'),
    path('post/contact/<pk>', views.PostContactDetailApiView.as_view(), name='postContactDetailView'),
    path('post/delete', views.PostDeleteApiView.as_view(), name='postDeleteView'),
    path('post/nocontact', views.PostContactFalse.as_view(), name='PostContactFalse'),
]
