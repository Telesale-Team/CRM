# Generated by Django 3.2.3 on 2023-05-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kpi', '0013_alter_thaiban_user_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thaiban',
            name='user_customer',
            field=models.CharField(max_length=20, verbose_name='username ลูกค้า '),
        ),
        migrations.AlterField(
            model_name='thaiban',
            name='user_telephone',
            field=models.CharField(max_length=10, verbose_name='เบอร์โทรลูกค้า '),
        ),
    ]