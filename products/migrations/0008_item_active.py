# Generated by Django 3.1.7 on 2021-03-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]