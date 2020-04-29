# Generated by Django 3.0.5 on 2020-04-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
