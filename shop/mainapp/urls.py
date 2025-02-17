from django.urls import path
from .views import homeView, aboutView, contactsView, AddProduct, ProductDetails, UpdateProduct, DeleteProduct   # importing the view from the mainapp to access the functions

urlpatterns =[
    path("", homeView, name='home'),
    path("about", aboutView, name='aboutpage'),
    path("contacts", contactsView, name='contactspage'),



path('products/add', AddProduct.as_view(), name = 'add_prod'),                # C
path('products/<int:pk>', ProductDetails.as_view(), name = 'prod_details'),   # R
path('products/edit/<int:pk>', UpdateProduct.as_view(), name = 'edit_prod'),  # U
path('products/del/<int:pk>', DeleteProduct.as_view(), name = 'det_prod')     # D
]
