# Generated by Django 3.2.20 on 2023-08-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_contact_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='not provided', max_length=100),
            preserve_default=False,
        ),
    ]
