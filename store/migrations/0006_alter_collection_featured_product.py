# Generated by Django 4.1.7 on 2023-03-14 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_orderitem_product_alter_product_collection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
    ]
