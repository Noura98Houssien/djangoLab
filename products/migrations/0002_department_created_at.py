# Generated by Django 3.1 on 2021-03-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]