# Generated by Django 4.2.2 on 2023-07-01 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Create_page',
        ),
        migrations.DeleteModel(
            name='Edit_Page',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='check_input_and_output',
            new_name='check_and_out',
        ),
    ]