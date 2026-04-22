from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='caterories')

    def __str__(self):
        return self.name    

class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='products')   
    stock = models.IntegerField()
    price = models.IntegerField()
    caterory = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name     
      