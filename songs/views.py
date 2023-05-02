from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from songs.serializers import SongSerializer
from songs.models import Song
from albums.models import Album
from rest_framework import generics


class SongListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "page_size"


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = SongListPagination

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(album_id=self.request.user.id)


# album_id = self.request.user.album
