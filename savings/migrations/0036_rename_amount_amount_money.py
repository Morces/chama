# Generated by Django 4.1.2 on 2022-10-27 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0035_remove_amount_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amount',
            old_name='amount',
            new_name='money',
        ),
    ]