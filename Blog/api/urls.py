from django.urls import path
from .views import *

urlpatterns = [
    # Users urls
    path('users/', UserViewSet.as_view()),
    path('users/<int:pk>/', UserUpdateDeleteViewSet.as_view()),

    # Posts url
    path('posts/', PostViewSet.as_view()),
    path('posts/<int:pk>/', PostUpdateDeleteViewSet.as_view()),

    # Likes url
    path('likes/', LikeViewSet.as_view()),
    path('likes/<int:pk>/', LikeUpdateDeleteViewSet.as_view()),
]
