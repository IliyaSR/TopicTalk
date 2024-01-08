# Generated by Django 5.0 on 2024-01-08 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_like_to_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='to_comment',
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
            ],
        ),
    ]
