# Generated by Django 2.2 on 2019-05-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandises', '0002_auto_20190519_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
