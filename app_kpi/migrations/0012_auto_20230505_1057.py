# Generated by Django 3.2.3 on 2023-05-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kpi', '0011_thaiban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thaiban',
            name='user_buy',
            field=models.BooleanField(default=False, verbose_name='ซื้อแล้ว/ยังไม่ซื้อ'),
        ),
        migrations.AlterField(
            model_name='thaiban',
            name='user_customer',
            field=models.CharField(max_length=255, verbose_name='username ลูกค้า '),
        ),
        migrations.AlterField(
            model_name='thaiban',
            name='user_password',
            field=models.CharField(max_length=255, verbose_name='password  ลูกค้า'),
        ),
        migrations.AlterField(
            model_name='thaiban',
            name='user_qutity',
            field=models.PositiveIntegerField(verbose_name='จำนวนการซื้อ'),
        ),
        migrations.AlterField(
            model_name='thaiban',
            name='user_telephone',
            field=models.CharField(max_length=255, verbose_name='เบอร์โทรลูกค้า '),
        ),
    ]
