from django.urls import path
from songs.views import SongView

urlpatterns = [
    path("songs/<int:pk>/", SongView.as_view()),
]
