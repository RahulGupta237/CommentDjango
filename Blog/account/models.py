
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
