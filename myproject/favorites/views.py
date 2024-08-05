# favorites/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Favorite, FavoriteStar
from .forms import FavoriteForm
from django.contrib.auth.decorators import login_required

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})

@login_required
def add_favorite(request):
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.user = request.user
            favorite.save()
            return redirect('favorite_list')
    else:
        form = FavoriteForm()
    return render(request, 'favorites/add_favorite.html', {'form': form})

@login_required
def toggle_favorite_star(request):
    if request.method == "POST":
        favorite_pk = request.POST.get('favorite_pk')
        action = request.POST.get('action')
        if favorite_pk and action == 'favorite':
            favorite_instance = get_object_or_404(Favorite, pk=int(favorite_pk))
            try:
                favorite_star = FavoriteStar.objects.get(favorite=favorite_instance)
                favorite_star.delete()
            except FavoriteStar.DoesNotExist:
                FavoriteStar.objects.create(favorite=favorite_instance)
    return redirect('favorite_list')