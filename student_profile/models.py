from django.contrib.auth.models import User
from django.db import models


class Student (models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(null=True)
    nro_institutional = models.CharField(max_length=60)
    profilePhoto = models.ImageField(upload_to='student_profile_photo')

    # Perfil
    ingress_year = models.IntegerField()
    graduate_year = models.IntegerField()
    course = models.CharField(max_length=60)

    # Outras redes
    github = models.URLField(null=True)
    linkedIn = models.URLField(null=True)
    lattes = models.URLField(null=True)

