from django.urls import path
from .views import ArtisteView
from .views import SongView

urlpatterns = [
    path('artiste/', ArtisteView),
    path('song/', SongView)
]