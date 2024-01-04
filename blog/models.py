from django.contrib.auth.models import User
from django.db import models
from common.models import BaseModel


class Blog(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
