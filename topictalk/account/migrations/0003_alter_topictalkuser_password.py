# Generated by Django 5.0 on 2024-01-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_topictalkuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topictalkuser',
            name='password',
            field=models.CharField(),
        ),
    ]