from django.urls import path
from .import views


urlpatterns = [
    path('login',views.Login.as_view(), name = 'signin'), # Login is class , Aas_view is function
    path('register', views.UserRegister.as_view(), name = 'signup') # as view use for when we are using class

]