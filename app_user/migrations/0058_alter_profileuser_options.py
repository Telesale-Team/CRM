# Generated by Django 3.2 on 2023-06-18 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0057_alter_profileuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileuser',
            options={'ordering': ['-username'], 'verbose_name': 'Member', 'verbose_name_plural': 'Profile'},
        ),
    ]