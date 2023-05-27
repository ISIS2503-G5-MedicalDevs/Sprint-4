from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IPSs_view, name='IPSs_view'),
    path('<int:pk>', views.IPS_view, name='IPS_view'),
    path('test', views.IPS_test, name= 'IPS_test'),
    path('test2', views.IPS_test2, name = 'IPS_test2')
]
