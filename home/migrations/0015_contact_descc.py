# Generated by Django 3.2.20 on 2023-08-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_contact_descc'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='descc',
            field=models.CharField(default='not', max_length=100),
            preserve_default=False,
        ),
    ]
