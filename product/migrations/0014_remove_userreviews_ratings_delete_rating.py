# Generated by Django 5.0.1 on 2024-01-18 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_userreviews_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreviews',
            name='ratings',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
