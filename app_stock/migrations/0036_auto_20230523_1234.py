# Generated by Django 3.2.3 on 2023-05-23 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0035_rename_item_name_cable_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='category',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='username',
        ),
        migrations.RemoveField(
            model_name='office',
            name='category',
        ),
        migrations.RemoveField(
            model_name='office',
            name='user_account',
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Create Cable'},
        ),
        migrations.RemoveField(
            model_name='stock',
            name='item',
        ),
        migrations.AddField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_stock.category'),
        ),
        migrations.AddField(
            model_name='stock',
            name='detail',
            field=models.TextField(max_length=255, null=True, verbose_name='อุปกรณ์เสริม'),
        ),
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=60, null=True, verbose_name='ชื่อสินค้า'),
        ),
        migrations.AddField(
            model_name='stock',
            name='serial',
            field=models.CharField(max_length=60, null=True, verbose_name='รหัสสินค้า'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateField(verbose_name='วันที่'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quatity',
            field=models.PositiveIntegerField(default=1, verbose_name='จำนวน'),
        ),
        migrations.DeleteModel(
            name='Cable',
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]
