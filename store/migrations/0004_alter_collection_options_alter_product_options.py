# Generated by Django 4.2.1 on 2023-05-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
    ]
