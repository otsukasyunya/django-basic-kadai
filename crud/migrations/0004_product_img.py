# Generated by Django 4.2.4 on 2023-09-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noimage.png', upload_to=''),
        ),
    ]
