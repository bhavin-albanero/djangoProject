from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "content", "timestamp", "updated", "user", "likes"]
