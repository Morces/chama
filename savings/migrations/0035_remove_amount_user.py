# Generated by Django 4.1.2 on 2022-10-27 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0034_amount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='user',
        ),
    ]
