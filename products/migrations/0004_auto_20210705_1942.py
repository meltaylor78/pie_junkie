# Generated by Django 3.2.4 on 2021-07-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_power'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.BooleanField(blank=True, max_length=254, null=True),
        ),
    ]
