# Generated by Django 4.1.2 on 2022-10-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0003_alter_savings_savings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='savings',
            field=models.CharField(max_length=100),
        ),
    ]
