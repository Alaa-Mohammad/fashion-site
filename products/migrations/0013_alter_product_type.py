# Generated by Django 3.2.8 on 2021-10-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('coat', 'coat'), ('jacket', 'jacket'), ('dresse', 'dresse'), ('shirt', 'shirt'), ('T-shirt', 'T-shirt'), ('jeans', 'jeans')], default='coat', max_length=15),
        ),
    ]
