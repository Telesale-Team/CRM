# Generated by Django 3.2.3 on 2023-04-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0015_auto_20230402_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='id_user',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
