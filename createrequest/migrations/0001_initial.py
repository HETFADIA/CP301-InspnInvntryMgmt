# Generated by Django 2.2.12 on 2022-03-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('date_of_delivery', models.DateField()),
                ('po_number', models.CharField(max_length=200)),
                ('po_date', models.CharField(max_length=200)),
                ('invoice_amount', models.FloatField(default=0)),
                ('invoice_number', models.TextField(default='')),
                ('invoice_link', models.TextField(default='')),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(default='')),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]