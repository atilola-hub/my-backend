from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, password, **extra_fields):
        if not email:
            raise TypeError("Email is required")
        if not fullname:
            raise TypeError("Fullname is required")
        if not phone:
            raise TypeError("Phone number is required")
        if not password:
            raise TypeError("Password is required")
        user = self.model(email=self.normalize_email(email), fullname=fullname, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise TypeError("Email is required")
        if not password:
            raise TypeError("Password is required")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


ACCOUNT_TYPES = [
    ("BUYER","Buyer"),
    ("SELLER", "Seller"),
    ("RIDER", "Rider"),
    ("MIDDLEMAN", "Middleman"),
    ("ADMIN", "Admin ")
]

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bvn = models.CharField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, default=ACCOUNT_TYPES[0][0])
    dob = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname", "phone"]
    objects = UserManager()

    def __str__(self):
        return self.fullname

    def token(self):
        refresh_token = RefreshToken.for_user(self)
        return {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
        }