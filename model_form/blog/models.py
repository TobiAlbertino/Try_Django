from django.db import models

# Create your models here.
from .validators import validate_author


class Post(models.Model):
    judul       =models.CharField(max_length = 100)
    body        =models.TextField()
    author      =models.CharField(
            max_length = 100,
            validators = [validate_author],
        )

    LIST_CATEGORY = (
        ('jurnal','jurnal'),
        ('blog','blog'),
        ('berita','berita'),
    )
    category    =models.CharField(
        max_length = 100,
        choices = LIST_CATEGORY,
        default = 'blog',
        )

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)