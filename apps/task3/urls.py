from django.urls import path
from .api_endpoints.Product.ProductCreate import ProductCreateAPIView
from .api_endpoints.Product.ProductList import ProductListAPIVIew

urlpatterns = [
    path("product-create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("product-list/", ProductListAPIVIew.as_view(), name="product-list"),
]
