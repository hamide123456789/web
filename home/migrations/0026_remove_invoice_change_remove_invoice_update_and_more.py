# Generated by Django 4.2.3 on 2023-07-14 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_invoice_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='change',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='update',
        ),
        migrations.DeleteModel(
            name='Chart',
        ),
    ]