from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import user_feed
from .views import like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('feed/', user_feed, name='user-feed'),
    path('posts/<int:post_id>/like/', like_post),
    path('posts/<int:post_id>/unlike/', unlike_post),
]