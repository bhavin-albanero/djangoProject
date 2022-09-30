from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PostLikeApiView,
)

urlpatterns = [
    path('posts/<int:post_id>/like', PostLikeApiView.as_view()),
    path('posts/<int:post_id>/like/<int:like_id>', PostLikeApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
