from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
