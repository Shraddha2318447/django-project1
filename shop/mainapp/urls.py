from django.urls import path
from . import views # importing the view from the mainapp to access the functions

urlpatterns =[
    path("", views.homeView, name='home'),
    path("about", views.aboutView, name='aboutpage'),
    path("contacts", views.contactsView, name='contactspage')
]
