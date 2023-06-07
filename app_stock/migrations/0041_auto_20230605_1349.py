# Generated by Django 3.2 on 2023-06-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0040_auto_20230604_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_status',
            field=models.CharField(blank=True, choices=[('ใช้งานได้', 'ใช้งานได้'), ('ชำรุด', 'ชำรุด')], default='ใช้งานได้', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_status',
            field=models.CharField(blank=True, choices=[('สต๊อก', 'สต๊อก'), ('ยืม', 'ยืม')], default='สต๊อก', max_length=100),
        ),
    ]