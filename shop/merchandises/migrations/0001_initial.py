# Generated by Django 2.2 on 2019-05-19 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=40)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchandises', to='sellers.Seller')),
            ],
        ),
    ]
