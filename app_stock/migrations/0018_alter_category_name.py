# Generated by Django 3.2.3 on 2023-05-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0017_auto_20230504_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, verbose_name='ชื่อหมวดหมู่'),
        ),
    ]