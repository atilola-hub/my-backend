from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "owner", "name", "category",
        #           "description", "price", "quantity", "image",
        #           "quantity_sold", "created_at", "updated_at"]
        read_only_fields = ["id", "quantity_sold", "created_at", "owner"]