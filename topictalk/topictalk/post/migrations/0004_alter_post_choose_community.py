# Generated by Django 5.0 on 2024-01-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_like_to_comment_likecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='choose_community',
            field=models.CharField(choices=[('League of Legends', 'League of Legends'), ('Minecraft', 'Minecraft'), ('NBA', 'NBA'), ('Premier League', 'Premier League'), ('Bitecoin', 'Bitecoin'), ('Litecoin', 'Litecoin')], max_length=20),
        ),
    ]
