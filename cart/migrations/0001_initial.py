# Generated by Django 4.0.2 on 2022-02-28 04:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('coupon_name', models.CharField(max_length=100, unique=True)),
                ('coupon_discount_amount', models.FloatField(default=0.2)),
                ('use_times', models.PositiveIntegerField(default=10)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0.1)),
                ('total_amt', models.FloatField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('coupon_applied', models.BooleanField(default=False)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_signature', models.CharField(blank=True, max_length=300, null=True)),
                ('invoice', models.FileField(blank=True, null=True, upload_to='invoice')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_cart', to='authentication.learnermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItemsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total', models.FloatField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_cart', to='cart.ordermodel')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_items', to='app.coursemodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_customer_cart_items', to='authentication.learnermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
