# Generated by Django 2.2 on 2019-05-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandises', '0003_auto_20190519_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]