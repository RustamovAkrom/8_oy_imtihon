from typing import Iterable
from django.db import models
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import base64


class Categories(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="images/product/", null=True, blank=True, default="images/product.png"
    )
    price = models.CharField(max_length=120)
    marja = models.CharField(max_length=120)
    package_code = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, models.CASCADE)

    def encryption(self, values: str):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(values.encode("utf-8"), AES.block_size))
        iv = base64.b64encode(cipher.iv)
        ct = base64.b64encode(ct_bytes)
        return key, iv, ct

    def decryption(self, iv, ct):
        key = get_random_bytes(16)
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        output = unpad(cipher.decrypt(ct), AES.block_size).decode("utf-8")
        return output

    def save(self, *args, **kwargs):
        price_key, price_iv, price_ct = self.encryption(str(self.price))
        marja_key, marja_iv, marja_ct = self.encryption(str(self.marja))
        package_code_key, package_code_iv, package_code_ct = self.encryption(
            self.package_code
        )

        self.price = price_ct
        self.marja = marja_ct
        self.package_code = package_code_ct

        self.price_key = base64.b64encode(price_key).decode("utf-8")
        self.marja_key = base64.b64encode(marja_key).decode("utf-8")
        self.package_code_key = base64.b64encode(package_code_key).decode("utf-8")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"


__all__ = (
    "Product",
    "Categories",
)
