# Generated by Django 4.2.1 on 2023-05-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderitem_orderitemname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cartnameitem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
