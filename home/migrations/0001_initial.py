# Generated by Django 3.0.7 on 2021-09-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=50)),
                ('collagename', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('mobilenum', models.IntegerField(max_length=12)),
            ],
        ),
    ]
