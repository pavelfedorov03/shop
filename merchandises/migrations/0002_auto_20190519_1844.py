# Generated by Django 2.2 on 2019-05-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandises', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchandise',
            name='name',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='text',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merchandise',
            name='title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
