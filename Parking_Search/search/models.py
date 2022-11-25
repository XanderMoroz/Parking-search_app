from django.db import models
from django.contrib.postgres.indexes import GinIndex
# Create your models here.

class ParkingPlace(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
    # class Meta:
    #     indexes = [GinIndex(name='full-text_index', fields=['title'], opclasses=['varchar_pattern_ops'])]
