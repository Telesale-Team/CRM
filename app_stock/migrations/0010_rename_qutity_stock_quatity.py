# Generated by Django 3.2.3 on 2023-05-02 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0009_auto_20230502_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='qutity',
            new_name='quatity',
        ),
    ]
