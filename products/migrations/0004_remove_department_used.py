# Generated by Django 3.1 on 2021-03-12 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_department_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='used',
        ),
    ]
