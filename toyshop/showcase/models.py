from django.db import models
import os
from uuid import uuid4
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string

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
    slug = models.SlugField('Toy slug', max_length=150, null=False, blank=False, unique=True, editable=False)
    image = models.ImageField(null=True, upload_to=path_and_rename, blank=True, default='default.jpg')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if Toy.objects.filter(name_en=self.name_en).exists():
            value = f'{self.name_en}_{get_random_string(length=4)}'
            self.slug = slugify(value, allow_unicode=True)
        else:
            self.slug = slugify(self.name_en, allow_unicode=True)
        super(Toy, self).save(*args, **kwargs)


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


class Order(models.Model):
    class Messengers(models.TextChoices):
        wa = 'whatsapp', 'WhatsApp'
        tg = 'telegram', 'Telegram'
        em = 'Email', 'e-mail'


    class OrderTypes(models.TextChoices):
        New = 'New toy order'
        Exist = 'Toy from shop'


    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    customer_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    preferable_messenger = models.CharField(max_length=10, choices=Messengers.choices, null=False, default='em')
    purchase_exist = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name='purchases', null=True)
    order_type = models.CharField(max_length=30, choices=OrderTypes.choices, null=True)
    comment = models.TextField(max_length=500, null=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f'#{self.id} - {self.customer_name} - {self.purchase_exist}'.replace('None', 'Custom Order')
    
    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('thank-you', kwargs=kwargs)
    
