# Generated by Django 5.0 on 2024-01-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_image_comment_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='link_description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='link_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]