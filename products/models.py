from django.db import models

class Products(models.Model):
    name_products=models.CharField(max_length=100)
    image=models.ImageField(upload_to="products/", blank=True, null=True)
    price=models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    TYPE_PRODUCTS=(
        ('bakery products', 'Bakery products'),
        ('grains and pasta', 'Grains and pasta'),
        ('meat products', 'Meat products'),
        ('dairy products', 'Dairy products'),
        ('vegetables', 'Vegetables')    
    )
    type_products=models.CharField(max_length=100, choices=TYPE_PRODUCTS )
    create_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_products

