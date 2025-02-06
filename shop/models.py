from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)  #модель для категории. CharField - текст, 255 - длина
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class Desideorio(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(blank=True, null=True) #число с плавающей точкой
    donat_qty = models.IntegerField(blank=True, null=True)
    comments_qty = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title