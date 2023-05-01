from rest_framework import serializers
from songs.models import Song


class SongSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Song:
        return Song.objects.create(**validated_data)

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "duration",
            "album_id",
        ]
        depth = 1
        read_only_fields = ["id, album_id"]
