# Generated by Django 3.2.3 on 2023-05-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0046_auto_20230506_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]