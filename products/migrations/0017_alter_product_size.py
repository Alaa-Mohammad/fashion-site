# Generated by Django 3.2.8 on 2021-10-30 11:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_priceafterdiscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('XS-S', 'XS-S'), ('M', 'M'), ('M-L', 'M-L'), ('L', 'L'), ('XL', 'XL')], max_length=22),
        ),
    ]
