from rest_framework.serializers import ModelSerializer
from apps.task3.models import Product


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "image",
            "price",
            "marja",
            "package_code",
            "created_at",
            "updated_at",
            "category",
        )
