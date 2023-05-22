

# Create your models here.
#company_logo = models.ImageField(upload_to='company_logos/',null=True)

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, mobile_number,profile_photo, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email, name, mobile_number, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, mobile_number=mobile_number,profile_photo=profile_photo,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, mobile_number,profile_photo, password=None, **extra_fields):
        """
        Creates and saves a new superuser with the given email, name, mobile_number, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, mobile_number,profile_photo, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to='profile_pic/',null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_number','profile_photo']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name



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
from django.urls import reverse

import random

def generate_uuid():
    return f'{random.randint(100, 999)}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='Comment')
    comment_text = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.CharField(max_length=3, unique=True, default=generate_uuid,blank=True,null=True)


    def __str__(self):
        return self.comment_text

    def created_at_display(self):
        time_difference = timezone.now() - self.created_at
        return naturaltime(time_difference)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.post.slug})




