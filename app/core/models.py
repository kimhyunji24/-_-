"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        user=self.create_user(email, password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()
    
    USERNAME_FIELD='email'

class Product(models.Model):
    product_name = models.CharField(max_length=255, default='Unknown') # 제품명
    product_kind = models.CharField(max_length=255, default='Unknown') # 유형명
    manufacture = models.CharField(max_length=255, default='Unknown') # 제조원
    allergy = models.TextField(default='Unknown') # 알레르기 유발 물질
    nutrient = models.TextField(default='Unknown') # 영양 성분
    product_img = models.URLField(null=True, blank=True) # 제품 이미지
    meta_img = models.URLField(null=True, blank=True) # 메타 이미지 (없어도 될 듯함.)

    def __str__(self):
        return self.product_name