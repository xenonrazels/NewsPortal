# Generated by Django 3.2.6 on 2021-08-21 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='authore',
            new_name='author',
        ),
    ]
