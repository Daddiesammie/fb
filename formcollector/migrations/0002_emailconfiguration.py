# Generated by Django 5.1.3 on 2024-11-22 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcollector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Gmail Address')),
                ('password', models.CharField(max_length=100, verbose_name='App Password')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]