# Generated by Django 4.0 on 2023-08-03 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_rename_name_customer_first_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Тұтынушы', 'verbose_name_plural': 'Тұтынушылар'},
        ),
    ]