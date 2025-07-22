from django.db import models

# Create your models here.
class User(models.Model):
    # id=models.IntegerField(max_length=50)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_brand=models.CharField(max_length=200)

    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.product_name
    