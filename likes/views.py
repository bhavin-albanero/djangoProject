from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Like
from .serializers import PostLikeSerializer


class PostLikeApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, like_id, user_id):
        """
        Helper method to get the object with given post_id, and user_id
        """
        try:
            return Like.objects.get(id=like_id, user=user_id)
        except Like.DoesNotExist:
            return None

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the post items for given requested user
        """
        todos = Like.objects.filter(user=request.user.id)
        serializer = PostLikeSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the post with given data
        """
        data = {
            'post': request.data.get('post_id'),
            'user': request.user.id
        }
        serializer = PostLikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, like_id, *args, **kwargs):
        """
        Deletes the post item with given post_id if exists
        """
        like_instance = self.get_object(like_id, request.user.id)
        if not like_instance:
            return Response(
                {"res": "Object with like id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        like_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
