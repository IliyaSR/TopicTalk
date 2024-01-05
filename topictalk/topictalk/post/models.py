from django.db import models

from topictalk.post.validators import validate_file_size


# Create your models here.
class Post(models.Model):
    Community = (
        ('League of legends', 'League of legends'),
        ('Minecraft', 'Minecraft'),
        ('NBA', 'NBA'),
        ('Premier League', 'Premier League'),
        ('Bitecoin', 'Bitecoin'),
        ('Litecoin', 'Litecoin')
    )
    choose_community = models.CharField(max_length=20, choices=Community)
    post_title = models.CharField(max_length=30)
    post_content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, validators=[validate_file_size])
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
