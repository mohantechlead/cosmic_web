# Generated by Django 5.0.6 on 2024-06-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier_profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='supplier_profile',
            name='supplier_name',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
