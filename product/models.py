from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.


class Size(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length = 100, null=True, blank=True, unique=True)
    def __str__(self):
        return self.name

class Color(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length = 100, null=True, blank=True, unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Clothing')
    image = models.ImageField(upload_to='media/',blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    size=models.ForeignKey(Size, on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserReviews(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"
    


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    