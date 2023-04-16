# Generated by Django 4.2 on 2023-04-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_introslide_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenefitCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cards/')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]
