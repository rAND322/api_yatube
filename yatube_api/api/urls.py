from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet


router_v1 = routers.DefaultRouter()
router_v1.register("posts", PostViewSet)
router_v1.register("groups", GroupViewSet)
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
