from django.db import models

from account.models import CustomUser
from PostApp.models import Post

from django.urls import reverse
from django.utils import timezone
import random
from django.contrib.humanize.templatetags.humanize import naturaltime
def generate_uuid():
    return f'{random.randint(100, 999)}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='Comment')
    comment_text = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.CharField(max_length=3, unique=True, default=generate_uuid,blank=True,null=True)
    is_edited=models.BooleanField(default=False)


    def __str__(self):
        return self.comment_text

    def created_at_display(self):
        time_difference = timezone.now() - self.created_at
        return naturaltime(time_difference)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.post.slug})



