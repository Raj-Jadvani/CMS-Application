from rest_framework import serializers
from .models import Auther, Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='post.author.user_id')  # to show author id

    class Meta:
        model = Like
        fields = '__all__'
