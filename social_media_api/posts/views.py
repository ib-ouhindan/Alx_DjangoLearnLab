from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from accounts.models import CustomUser
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post, Like
from django.contrib.auth import get_user_model
from notifications .utils import create_notification
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#"permissions.IsAuthenticated", "generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"]
@api_view(['GET'])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by.('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

#permissions.IsAuthenticated
@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if Like.objects.filter(user=user, post=post).exists():
        return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
    Like.objects.create(user=user, post=post)
    # Create a notification here
    create_notification(user, post.author, 'liked', post)
    return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    like = Like.objects.filter(user=user, post=post).
    if like.exists():
        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
