# Generated by Django 3.2.16 on 2022-12-20 12:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('tel_number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('explanation', models.CharField(max_length=100)),
                ('discount_percent', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_quantity', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('explanation', models.TextField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.discount')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.price')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_name', models.CharField(max_length=100)),
                ('pc_explanation', models.CharField(max_length=100)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_amount', models.IntegerField()),
                ('expiration_date', models.DateField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totall_payment', models.IntegerField()),
                ('payment_method', models.CharField(max_length=100)),
                ('tracking_number', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('bank_name', models.CharField(max_length=100)),
                ('purchase_amount', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('birthday_date', models.DateField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.address')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product_stock'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.address')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totall_payment', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.address')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
