# Generated by Django 3.2.20 on 2023-08-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contact_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(blank=True, default='Not Provided'),
        ),
    ]
