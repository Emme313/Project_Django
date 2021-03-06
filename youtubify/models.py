from django.db import models
from embed_video.fields import EmbedVideoField

class User(models.Model):
    username = models.CharField(max_length=100)
    profile = models.CharField(max_length=500)

    def __str__(self):
        return self.username

class Video(models.Model):
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    video_url = EmbedVideoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.song