from rest_framework.generics import CreateAPIView
from apps.task3.models import Product
from .serialisers import ProductCreateSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


__all__ = ("ProductCreateAPIView",)
