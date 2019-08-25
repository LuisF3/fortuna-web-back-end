# Generated by Django 2.2.4 on 2019-08-25 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_profile', '0001_initial'),
        ('company_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('requirements', models.TextField(null=True)),
                ('differentials', models.TextField(null=True)),
                ('local', models.CharField(max_length=60)),
                ('pay', models.IntegerField(null=True)),
                ('work_load', models.IntegerField()),
                ('work_time', models.CharField(max_length=60)),
                ('offer_end', models.DateField()),
                ('subscription_way', models.CharField(max_length=60)),
                ('likes_number', models.IntegerField(default=0)),
                ('ingress_year', models.IntegerField(null=True)),
                ('graduate_year', models.IntegerField(null=True)),
                ('course', models.CharField(max_length=60, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company_profile.Company')),
                ('liker_students', models.ManyToManyField(blank=True, related_name='liked_jobs', to='student_profile.Student')),
            ],
        ),
    ]
