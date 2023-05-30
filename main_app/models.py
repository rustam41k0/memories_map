from django.contrib.gis.db import models
from django.conf import settings


class Memory(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    location = models.PointField(verbose_name='Локация')

    def __str__(self):
        return self.title
