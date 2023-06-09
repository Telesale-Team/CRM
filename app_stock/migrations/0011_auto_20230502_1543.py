# Generated by Django 3.2.3 on 2023-05-02 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0010_rename_qutity_stock_quatity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'name',
                'verbose_name_plural': '',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': ''},
        ),
        migrations.AddField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_stock.category'),
        ),
    ]
