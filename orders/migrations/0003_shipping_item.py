# Generated by Django 5.0.6 on 2024-07-15 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_item_codes'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipping_item',
            fields=[
                ('id_numeric', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('item_name', models.TextField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('measurement', models.TextField(blank=True, null=True)),
                ('bags', models.FloatField(blank=True, null=True)),
                ('net_weight', models.FloatField(blank=True, null=True)),
                ('gross_weight', models.FloatField(blank=True, null=True)),
                ('order_no', models.ForeignKey(blank=True, db_column='order_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.cosmic_order')),
            ],
        ),
    ]