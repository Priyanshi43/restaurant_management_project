from django.db import models
fromdjango.contrib.auth.models import User
from restaurant_management.models import Menu

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)

class Order(models.Model):
    customer = models.foreignkey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amounte = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=''pending
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order #{self.id} - {self.customer.username}"