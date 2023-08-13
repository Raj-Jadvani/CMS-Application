from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Auther, Post, Like
from .permissions import *
from .serializers import *


# This class for Users get and post method
class UserViewSet(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        queryset = Auther.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            encrypted_password = make_password(serializer.validated_data['password'])  # convert to hash password
            serializer.validated_data['password'] = encrypted_password
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class for Retrive specific Users get and update and delete method
class UserUpdateDeleteViewSet(APIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return Auther.objects.get(pk=pk)
        except Auther.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = self.serializer_class(queryset)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        get_data = self.get_object(pk)
        serializer = self.serializer_class(get_data, data=request.data)
        if serializer.is_valid():
            encrypted_password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = encrypted_password
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_data = self.get_object(pk)
        get_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# This class for Post get and post method
class PostViewSet(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        queryset = Post.objects.filter(is_private=False).all()
        serialized_posts = []
        for post in queryset:
            serializer = self.serializer_class(post)
            serialized_post = serializer.data

            # Get the number of likes for this post
            num_likes = Like.objects.filter(post=post).count()  # get count for specific post
            serialized_post['num_likes'] = num_likes

            serialized_posts.append(serialized_post)

        return Response(serialized_posts, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class for Retrive specific Post get and update and delete method
class PostUpdateDeleteViewSet(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]    # add custom permission to only owners of a post to edit/delete it.

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if not queryset.is_private or queryset.author == request.user:
            serializer = self.serializer_class(queryset)
            serialized_data = serializer.data
            num_likes = Like.objects.filter(post=queryset).count()  # get count for specific post
            serialized_data['num_likes'] = num_likes
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied("You are not allowed to access this post.")

    def put(self, request, pk, format=None):
        get_data = self.get_object(pk)
        serializer = self.serializer_class(get_data, data=request.data)
        if serializer.is_valid():
            if get_data.author == request.user:
                serializer.save()
                serialized_data = serializer.data
                return Response(serialized_data, status=status.HTTP_200_OK)
            else:
                raise PermissionDenied("You are not the owner of this post.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_data = self.get_object(pk)
        if get_data.author == request.user:
            get_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied("You are not the owner of this post.")


# This class for Likes get and post method
class LikeViewSet(APIView):
    serializer_class = LikeSerializer

    def get(self, request, format=None):
        queryset = Like.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class for Retrive specific Likes get and update and delete method
class LikeUpdateDeleteViewSet(APIView):
    serializer_class = LikeSerializer

    def get_object(self, pk):
        try:
            return Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = self.serializer_class(queryset)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        get_data = self.get_object(pk)
        serializer = self.serializer_class(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_data = self.get_object(pk)
        get_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
