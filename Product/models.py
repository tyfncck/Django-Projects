from django.db import models

class Product(models.Model):
    #productapp için başlık değişkeni, max uzunluk 50
    title = models.CharField(max_length=50)
    #productapp için image değişkeni, eklenen fotoğraf konumu
    image = models.ImageField(upload_to='uploads/')
