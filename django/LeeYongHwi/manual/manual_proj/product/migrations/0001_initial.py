# Generated by Django 5.0.6 on 2024-06-12 02:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("productId", models.AutoField(primary_key=True, serialize=False)),
                ("productName", models.CharField(max_length=128)),
                ("productDescription", models.TextField()),
                ("productPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("productImage", models.CharField(max_length=100, null=True)),
                ("registeredDate", models.DateTimeField(auto_now_add=True)),
                ("updatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]
