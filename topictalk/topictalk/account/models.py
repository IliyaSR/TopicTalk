from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class TopicTalkUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.URLField()
