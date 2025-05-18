from django.contrib import admin
from django.urls import path,include
from .views import index,search_contacts,create_contact,delete_contact
app_name = 'contacts'
urlpatterns = [
    path('',index,name='index'),
    path('search/',search_contacts,name='search'),
    path('create-contact/',create_contact,name='create_contact'),
    path('delete-contact/<int:pk>/',delete_contact,name='delete_contact'),

]