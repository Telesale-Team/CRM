# Generated by Django 3.2.3 on 2023-05-05 17:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_kpi', '0016_auto_20230505_1721'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thaiban',
            new_name='Customer_Interest',
        ),
    ]
