# Generated by Django 3.2.3 on 2023-05-09 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_stock', '0022_auto_20230509_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='password_login',
            field=models.CharField(max_length=60, null=True, verbose_name='รหัสล็อคอิน'),
        ),
        migrations.AlterField(
            model_name='item',
            name='user_login',
            field=models.CharField(max_length=60, null=True, verbose_name='ชื่อล็อคอิน'),
        ),
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=60, null=True)),
                ('quatity', models.PositiveIntegerField(default=0)),
                ('detail', models.TextField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('user_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Stock',
            },
        ),
    ]
