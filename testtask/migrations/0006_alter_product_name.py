# Generated by Django 3.2 on 2022-07-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtask', '0005_alter_product_height_alter_product_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
