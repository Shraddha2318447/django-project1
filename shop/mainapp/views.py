from django.shortcuts import render
from .models import Product

# to hepl to load the templete file
from django.template import loader

# to hepl to return http response to the user for any given request
from django.http import HttpResponse
# Create your views here.

def homeView(request):
    # quering the DB and getting a collection of product class objects from the records
    products = Product .objects.all() # select * from product;

    # creating a context dictionary  to be used to render the templete eith info
    context = {
        'product_list' : products # the key we craete here, 
                                  # will be available as a variable in template desing
                                  # in 'home.html
    }
    templete = loader.get_template('home.html')
    return HttpResponse(templete.render(context, request))

def aboutView(request):

    context = {
          # here not give any dictionary means products
        'name' : "krishna",
        'students' : [
            "shraddha",
            "shivani",
            "deepak"
             ],
        'slept' : True
    }
    templete = loader.get_template('about.html')
    return HttpResponse(templete.render(context, request))

def contactsView(request):

    context = {
          
    }
    templete = loader.get_template('contacts.html')
    return HttpResponse(templete.render(context, request))

