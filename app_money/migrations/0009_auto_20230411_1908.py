# Generated by Django 3.2.3 on 2023-04-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_money', '0008_auto_20230411_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptinvoice',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='receiptinvoice',
            name='image2',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_money'),
        ),
        migrations.AddField(
            model_name='receiptinvoice',
            name='image3',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_money'),
        ),
        migrations.AddField(
            model_name='receiptinvoice',
            name='image4',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_money'),
        ),
        migrations.AddField(
            model_name='receiptinvoice',
            name='image5',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_money'),
        ),
    ]
