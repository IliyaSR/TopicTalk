from django.db import models

from topictalk.account.models import TopicTalkUser
from topictalk.post.validators import validate_file_size


# Create your models here.
class Post(models.Model):
    Community = (
        ('League of Legends', 'League of Legends'),
        ('Minecraft', 'Minecraft'),
        ('NBA', 'NBA'),
        ('Premier League', 'Premier League'),
        ('Bitecoin', 'Bitecoin'),
        ('Litecoin', 'Litecoin')
    )
    choose_community = models.CharField(max_length=20, choices=Community)
    post_title = models.CharField(max_length=30)
    post_content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True, validators=[validate_file_size])
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(TopicTalkUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ['-date_time_of_publication']


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class LikeComment(models.Model):
    to_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
