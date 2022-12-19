from rest_framework import serializers

from .models import Album
from users.serializers import UserSerializer

"""
# class AlbumSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     year = serializers.IntegerField()
#     user_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         return Album.objects.create(**validated_data)

"""

class AlbumSerializer(serializers.ModelSerializer):

    # user = UserSerializer(read_only=True)

    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj:Album ) -> str:
        # ipdb.set_trace()
        return obj.user_id

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
    
    