# Generated by Django 3.2.3 on 2023-05-09 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_stock', '0029_auto_20230509_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
