# Generated by Django 4.1.2 on 2022-10-13 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0012_savings_balance_delete_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savings',
            name='balance',
        ),
    ]
