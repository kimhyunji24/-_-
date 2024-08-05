# favorites/views.py
from django.shortcuts import render, redirect
from .models import Favorite
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