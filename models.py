from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=22,primary_key=True)
    product_name = models.CharField(max_length=20)
    product_description = models.CharField(max_length=200)
    product_posted_by = models.CharField(max_length=200)

# class contact_info(models.Model):
#     address =  models.CharField(max_length=22)
#     mobile = models.CharField(max_length=22)
#     email = models.CharField(max_length=22)