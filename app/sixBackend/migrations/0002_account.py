# Generated by Django 2.2.7 on 2019-12-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_username', models.CharField(max_length=100)),
                ('product_email', models.EmailField(max_length=100)),
                ('product_options', models.CharField(max_length=8)),
            ],
        ),
    ]