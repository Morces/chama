# Generated by Django 4.1.2 on 2022-10-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0022_balance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='savings',
            field=models.IntegerField(),
        ),
    ]
