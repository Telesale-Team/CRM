# Generated by Django 3.2.3 on 2023-06-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='check',
        ),
        migrations.AlterField(
            model_name='sale',
            name='check_user',
            field=models.BooleanField(default=True),
        ),
    ]