from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PostListApiView,
    PostDetailApiView,
    UserPostApiView,
)

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/<int:post_id>/', PostDetailApiView.as_view()),
    path('posts/user/<int:user_id>/', UserPostApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
