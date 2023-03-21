<<<<<<< HEAD
# Generated by Django 4.0.5 on 2023-03-06 20:35

from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 4.0.5 on 2023-03-21 17:45

from django.db import migrations, models
>>>>>>> main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('users', '0004_profile_image'),
        ('base', '0011_product_image'),
=======
>>>>>>> main
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=10)),
                ('post_address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('card_number', models.CharField(max_length=12)),
                ('card_exp_month', models.CharField(max_length=2)),
                ('card_exp_year', models.CharField(max_length=2)),
                ('card_ccs', models.CharField(max_length=3)),
                ('payment_date', models.DateTimeField(editable=False)),
                ('payment_number', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('cart_item', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=20)),
                ('ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('cart_items', models.ManyToManyField(to='cart.shoppingcartitem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
=======
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> main
            ],
        ),
    ]
