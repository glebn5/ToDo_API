from django.db import models

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length=255, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name='Описание')
    checked = models.BooleanField(blank=True, verbose_name='Выполнено')
    date_create = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Дата создания таски')

    def __str__(self):
        return self.task