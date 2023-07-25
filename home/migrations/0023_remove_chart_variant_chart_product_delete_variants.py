# Generated by Django 4.2.3 on 2023-07-13 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_variants_remove_chart_product_chart_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='variant',
        ),
        migrations.AddField(
            model_name='chart',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='v_overdue_account', to='home.product'),
        ),
        migrations.DeleteModel(
            name='variants',
        ),
    ]
