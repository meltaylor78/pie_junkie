# Generated by Django 3.2.4 on 2021-08-04 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_cust_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cust_review',
            name='name',
        ),
    ]
