from captcha.models import CaptchaStore
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin
)

from comment.models import CommentModel
from comment.serializers import CommentSerializer


class CommentsPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 25


class CommentViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = (
        CommentModel.objects.select_related("user", "record").all()
    )
    serializer_class = CommentSerializer
