from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length = 255, blank=True)
    body = models.TextField()
    email = models.EmailField(default='nama@web.com')
    alamat = models.CharField(max_length=255, blank=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length= 255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now= True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()

    def __str__(self):
        return "ID-> {}. judul->{}".format(self.id, self.judul)