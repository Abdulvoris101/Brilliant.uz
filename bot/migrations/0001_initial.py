# Generated by Django 4.0.10 on 2023-04-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegramId', models.BigIntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phoneNumber', models.BigIntegerField()),
                ('language', models.CharField(max_length=255)),
            ],
        ),
    ]
