# Generated by Django 5.0.1 on 2024-01-18 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_rating_value_alter_userreviews_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviews',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
