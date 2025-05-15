from django.contrib import admin
from django.urls import path,include
from .views import index,search_contacts

urlpatterns = [
    path('',index,name='index'),
    path('search',search_contacts,name='search'),

]