# Generated by Django 3.2.3 on 2023-05-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kpi', '0012_auto_20230505_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thaiban',
            name='user_buy',
            field=models.BooleanField(default=False, verbose_name='สมัครซื้อแล้ว'),
        ),
    ]
