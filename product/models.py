from django.db import models
import uuid
from authentication.models import User

PRODUCT_CATEGORIES = [
    ("OTHERS", "Others"),
    ("ELECTRONICS", "Electronics"),
    ("HOUSEHOLD", "Household"),
    ("KITCHEN", "Kitchen"),
    ("GADGETS", "Gadgets")
]

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=15, choices=PRODUCT_CATEGORIES, default=PRODUCT_CATEGORIES[0][0])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    quantity_sold = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
