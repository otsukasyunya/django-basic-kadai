from django.urls import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    img = models.ImageField(blank=True,default='noimage.png')

    def __str__(self):
         return self.name
    
    #新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')
