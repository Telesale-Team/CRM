# Generated by Django 3.2.3 on 2023-05-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0031_auto_20230502_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='create_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
