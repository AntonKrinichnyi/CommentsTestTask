from captcha.models import CaptchaStore
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.views import APIView
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
        CommentModel.objects.all().select_related("user", )
    )
    serializer_class = CommentSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "base.html"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {
            "comments": queryset,
        }
        return Response(context)


class CaptchaView(APIView):
    def get(self, request: Request):
        key = CaptchaStore.generate_key()
        image_url = request.build_absolute_uri(
            reverse("captcha-image", kwargs={"key": key})
        )
        return Response(
            {
                "key": key,
                "image_url": image_url,
            }
        )
