# Generated by Django 3.2.16 on 2022-12-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_wallet_wallet_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_comment',
            name='comment_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_like',
            name='like_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_number',
            field=models.IntegerField(null=True),
        ),
    ]
