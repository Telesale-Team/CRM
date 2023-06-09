# Generated by Django 3.2.3 on 2023-03-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_profile'),
        ),
    ]
