# Generated by Django 4.1.2 on 2022-10-13 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('savings', '0007_remove_savings_balance_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='paid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
