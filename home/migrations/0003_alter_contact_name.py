# Generated by Django 3.2.20 on 2023-08-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230802_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
