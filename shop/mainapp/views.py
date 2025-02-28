from django.shortcuts import render
from .models import Product

# importing url resolution tools
from django.urls import reverse , reverse_lazy


# to hepl to load the templete file
from django.template import loader

# to hepl to return http response to the user for any given request
from django.http import HttpResponse



# importing the genric class based views for CRUD operations
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
def homeView(request):
    # quering the DB and getting a collection of product class objects from the records
    products = Product .objects.all() # select * from product;

    # creating a context dictionary  to be used to render the templete eith info
    context = {
        'product_list' : products, # the key we craete here, 
                                  # will be available as a variable in template desing
                                  # in 'home.html
        'current_page' : 'home'                         
    }
    templete = loader.get_template('home.html')
    return HttpResponse(templete.render(context, request))

def aboutView(request):

    context = {
          # here not give any dictionary means products
        'current_page' : 'about'
    }
    templete = loader.get_template('about.html')
    return HttpResponse(templete.render(context, request))

def contactsView(request):

    context = {
          
    }
    templete = loader.get_template('contacts.html')
    return HttpResponse(templete.render(context, request))

# below we use class based view, classe cannot run 

class AddProduct(CreateView): # http method- get method
    model = Product
    fields = ['name', 'price', 'desc', 'pic', 'stock']
    template_name = 'addproduct.html'
    success_url = reverse_lazy('home') # where should i take u that one is success url

    # Read -> show details of each product
class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

    # update ->
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__' # all means name, price, desc, pic and stock in that like that above AddProduct
    template_name = 'editProduct.html'

    # overriding a method to produce dynamic redirection according to product id.
    def get_success_url(self):
        return reverse('prod_details', kwargs = {"pk" : self.object.pk})  # pk-primarykey
    
    #Delete

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delProduct.html'
    success_url = reverse_lazy('home')

# Search results
def searchView(request):
    query = request.GET.get('search_text')
    # fetch the query text form GET request

    results = Product.objects.filter(name__icontains = query)
    # collect the peoduct object matching the come
    # this runs 'SELECT' FORM product WHERE name like '%<query>%'    
    # icontains is case_insensitive
    # contains can be used for case-sensitive


    context = {
        'items' : results,
        'query' : query
    }
    template = loader.get_template('searchResults.html')
    return HttpResponse(template.render(context, request))
       
