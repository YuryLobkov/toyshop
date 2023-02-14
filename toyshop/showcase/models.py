from django.db import models

# Create your models here.


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

    def __str__(self):
        return self.name
    


class Materials(models.Model):
    material = models.CharField(max_length=30)

class Sizes(models.Model):
    size = models.CharField(max_length=20)

class Categories(models.Model):
    category = models.CharField(max_length=50)
