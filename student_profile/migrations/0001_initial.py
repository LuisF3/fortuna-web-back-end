# Generated by Django 2.2.4 on 2019-08-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nro_institutional', models.CharField(max_length=60)),
                ('profilePhoto', models.ImageField(upload_to='student_profile_photo')),
                ('ingress_year', models.IntegerField()),
                ('graduate_year', models.IntegerField()),
                ('course', models.CharField(max_length=60)),
                ('github', models.URLField(null=True)),
                ('linkedIn', models.URLField(null=True)),
                ('lattes', models.URLField(null=True)),
            ],
        ),
    ]