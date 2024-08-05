# favorites/models.py
from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()

    def is_favorited(self):
        return FavoriteStar.objects.filter(favorite=self).exists()

class FavoriteStar(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='like_favorite')