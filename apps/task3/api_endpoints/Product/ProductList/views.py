from rest_framework.generics import ListAPIView
from apps.task3.models import Product
from .serializers import ProductListSerializer


class ProductListAPIVIew(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


__all__ = ("ProductListAPIVIew",)
