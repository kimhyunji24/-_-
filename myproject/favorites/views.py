# favorites/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Favorite, FavoriteStar
from .serializers import FavoriteSerializer

@api_view(['GET'])
def favorite_list(request):
    favorites = Favorite.objects.all()
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_favorite(request):
    serializer = FavoriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def toggle_favorite_star(request, pk):
    favorite = get_object_or_404(Favorite, pk=pk)
    try:
        star = FavoriteStar.objects.get(favorite=favorite)
        star.delete()
        return Response({'message': 'Favorite star removed.'}, status=status.HTTP_200_OK)
    except FavoriteStar.DoesNotExist:
        FavoriteStar.objects.create(favorite=favorite)
        return Response({'message': 'Favorite star added.'}, status=status.HTTP_201_CREATED)