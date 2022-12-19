from rest_framework import serializers

from albums.serializers import AlbumSerializer

from .models import Song


class SongSerializer(serializers.ModelSerializer):
     
#      album = AlbumSerializer(read_only=True)
     
    album_id = serializers.SerializerMethodField()

    def get_album_id(self, obj:Song ) -> str:
        # ipdb.set_trace()
        return obj.album_id

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]

        # read_only_fields = ["album"]


# class SongSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     duration = serializers.CharField(max_length=255)
#     album_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         return Song.objects.create(**validated_data)