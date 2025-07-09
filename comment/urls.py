from django.urls import path, include
from rest_framework import routers

from comment.views import CommentViewSet

app_name = "comment"

router = routers.DefaultRouter()

router.register("comment", CommentViewSet)

urlpatterns = [
    path("comments", include(router.urls))
]

