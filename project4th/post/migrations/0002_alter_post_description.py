# Generated by Django 5.1.4 on 2025-04-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
