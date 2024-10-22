# favorites/models.py

from django.db import models

class Favorite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 필드 추가

    def is_favorited(self):
        return FavoriteStar.objects.filter(favorite=self).exists()

class FavoriteStar(models.Model):
    favorite = models.ForeignKey(Favorite, related_name='stars', on_delete=models.CASCADE)