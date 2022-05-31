from django.db import models
from apps.category.models import Category
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='products')
    watch = models.PositiveIntegerField(default=0)

    def str(self) -> str:
        return self.title


# class LikeProduct(models.Model):
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
#     product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="likes")
#     is_like = models.BooleanField(default=True)
