# Generated by Django 3.2.3 on 2023-05-31 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sale', '0009_alter_sale_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='buy',
            field=models.CharField(blank=True, choices=[('ซื้อ', 'ซื้อ'), ('ยังไม่ซื้อ', 'ยังไม่ซื้อ')], default='ยังไม่ซื้อ', max_length=50, verbose_name='ซื้อ หรือ ไม่ซื้อ ?'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='call_back',
            field=models.CharField(blank=True, choices=[('Line', 'Line'), ('Facebook', 'Facebook'), ('Tiktok', 'Tiktok'), ('Youtube', 'Youtube'), ('Website', 'Website'), ('Other', 'Other')], max_length=100, null=True, verbose_name='ช่องทางติดต่อกลับ'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='name',
            field=models.CharField(max_length=255, verbose_name='ชื่อลูกค้า'),
        ),
    ]