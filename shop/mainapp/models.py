from django.db import models

# Create your models here.
# In the models nodule imported above, there is a class called 'model.
# Automatic ORM(Object Relational Mapping) methods are already pre-desinged in this class


# now let's create the shema for our project
# we need products
# any time we make any changes in the class definitions, especially the variables, 
# we need to run two commands.
# 1. python manage.py makemigrations

#   -> This generates python scripts inside the app's migrations folder.
#   -> It will track the models.py and check for changes. 
class Product(models.Model):
    # list out all the object variable below and initialize with certian classes
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(null=False)
    desc = models.TextField()
    pic = models.ImageField(upload_to="products/", null = False)
    stock = models.PositiveBigIntegerField(default= 1)
