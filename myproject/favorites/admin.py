# favorites/admin.py
from django.contrib import admin
from .models import Favorite, FavoriteStar

admin.site.register(Favorite)
admin.site.register(FavoriteStar)