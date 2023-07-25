# Generated by Django 4.2.3 on 2023-07-12 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_invoice_date_of_cash_deposit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_of_cash_deposit',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_of_contract',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=300, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('contract_price', models.IntegerField(default=0)),
                ('Invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pr_update', to='home.invoice')),
            ],
        ),
    ]
