# Generated by Django 4.1.7 on 2023-03-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_temp', '0002_alter_temperature_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='month',
            field=models.IntegerField(),
        ),
    ]
