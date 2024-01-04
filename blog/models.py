from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from common.models import BaseModel


class Blog(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def slugify(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(self).save()
