# Generated by Django 3.2.16 on 2023-02-21 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='category',
            name='explanation',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modified_date',
        ),
    ]
