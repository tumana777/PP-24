from django.db import models


class BaseManager(models.Manager):

    def get_new_cars(self):
        return self.get_queryset().filter(year__gt=2018)