from django.db import models

class Basket(models.Model):
    product_name=models.CharField(max_length=100, verbose_name= 'Напишите, что вы ищете ?')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('🚚', '🚚'),
        ('🏪', '🏪')
    )
    status_delivery= models.CharField(max_length=100, verbose_name='Как вы бы хотели получить товар?', choices=STATUS)
    
    def __str__(self):
        return f'{self.product_name} - {self.quantity} шт - {self.status_delivery}'