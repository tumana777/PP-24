from django.db import models
from core.managers import BaseManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(verbose_name="მწარმოებელი", max_length=15, null=False, blank=False)
    model = models.CharField(max_length=15, null=False, blank=False)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("core.Category", on_delete=models.SET_NULL, null=True, related_name='cars')
    is_sold = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10000)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='car_images/', default='car_images/default.png')

    class Meta:
        db_table = "car"
        verbose_name_plural = "car"

    def __str__(self):
        return f"{self.make} {self.model}"

    objects = BaseManager()