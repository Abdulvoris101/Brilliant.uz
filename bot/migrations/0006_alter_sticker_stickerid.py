# Generated by Django 4.0.10 on 2023-04-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='stickerId',
            field=models.TextField(),
        ),
    ]
