# Generated by Django 4.2.3 on 2023-07-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_invoice_change_remove_invoice_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='update',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='update',
            field=models.DateField(auto_now=True),
        ),
    ]