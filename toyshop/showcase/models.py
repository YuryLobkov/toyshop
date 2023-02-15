from django.db import models
import os
from uuid import uuid4

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'toys_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Toy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    material = models.ForeignKey('Materials', on_delete=models.CASCADE)
    size = models.ForeignKey('Sizes', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(null=True, upload_to=path_and_rename, blank=True, default='default.jpg')

    def __str__(self):
        return self.name
    

class Materials(models.Model):
    material = models.CharField(max_length=30)

    def __str__(self):
        return self.material
    

class Sizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size
    

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category



class Customer(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    purchase = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name='purchases', null=True)
    order = models.TextField(max_length=500, null=True)
    comment = models.TextField(max_length=500, null=True)
