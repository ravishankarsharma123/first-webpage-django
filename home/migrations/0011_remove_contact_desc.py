# Generated by Django 3.2.20 on 2023-08-02 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_contact_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]
