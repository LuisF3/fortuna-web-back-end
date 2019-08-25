from django.db import models

from company_profile.models import Company
from student_profile.models import Student


class Job(models.Model):
    title = models.CharField(max_length=60)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    description = models.TextField()
    requirements = models.TextField(null=True)
    differentials = models.TextField(null=True)


    # Details
    local = models.CharField(max_length=60)
    pay = models.IntegerField(null=True)
    work_load = models.IntegerField()
    work_time = models.CharField(max_length=60)
    offer_end = models.DateField()
    subscription_way = models.CharField(max_length=60)

    # Likes
    liker_students = models.ManyToManyField(Student, related_name='liked_jobs', blank=True)
    likes_number = models.IntegerField(default=0)

    # Perfil
    ingress_year = models.IntegerField(null=True)
    graduate_year = models.IntegerField(null=True)
    course = models.CharField(max_length=60, null=True)
