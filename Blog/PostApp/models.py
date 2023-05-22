from django.db import models
from account.models import CustomUser
# Create your models here.
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

import uuid
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField()
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.IntegerField(default=0)
    # like_count = models.PositiveIntegerField(default=0)
    is_edited=models.BooleanField(default=False)
    

    # uuid = models.UUIDField(default=uuid.uuid4, editable=False,blank=True,null=True)
    # other fields in your model

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def created_at_display(self):
        time_difference = timezone.now() - self.created_at
        return naturaltime(time_difference)

    def __str__(self):
        return self.title