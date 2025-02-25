from django.db import models

# CartItem table will have two foreign keys
# 1. Product id
from mainapp.models import Product

# 2. User id
from django.contrib.auth.models import User

# Create your models here.

# Let's model a cartitem

class CartItem(models.Model):
    # 1. Product to CartItem has a one to many relation, this is represented by a foreign key constraint
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Above, the 'one_delete = model.CASECADE' will ensure the all caritems are deleted when a  related Product is deleted

    # 2. User to CartItem has a one to many relationship, again reperesented by a foreign key constrain
    # Here aslo, we ensure that a certitem ia deleted automatocally if the user is deleted from the website.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 3. Quntity of the specific item in cart
    quantity = models.PositiveBigIntegerField(default=0)

    # 4. Date when the product was added to cart
    date_added = models.DateField(auto_now_add=True)

    # Starting reperesentation of CartItem object
    def __str__(self):
        return f"Product: {self.product.name} - Count: {self.quantity}" 
    
    # method to find total price of particular itr=em in cart
    def get_total_price(self):
        return self.quantity * self.product.price
