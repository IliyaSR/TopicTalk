from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    link_description = models.TextField(blank=True, null=True)
    date_of_publication = models.DateField(auto_now=True)