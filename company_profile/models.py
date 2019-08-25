from django.contrib.auth.models import User
from django.db import models


class Company (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(null=True)
    cnpj = models.CharField(max_length=15)
    site = models.URLField(null=True)
    contact = models.CharField(max_length=60)
    description = models.TextField()
    profilePhoto = models.ImageField(upload_to='company_profile_photo')
