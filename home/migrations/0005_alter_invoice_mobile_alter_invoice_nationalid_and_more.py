# Generated by Django 4.2.2 on 2023-07-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='mobile',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='nationalid',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='telephone',
            field=models.CharField(max_length=300),
        ),
    ]