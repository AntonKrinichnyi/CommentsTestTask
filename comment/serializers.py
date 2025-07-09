from django.contrib.auth import get_user_model
from rest_framework import serializers

from comment.models import CommentModel

User = get_user_model()


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False,
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "user",
            "text",
            "created_at",
            "images"
        )


class CommentSerializer(serializers.ModelSerializer):
    child = RecordSerializer(
        many=True,
        read_only=True
    )
    user = serializers.SlugRelatedField(
        many=False,
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "user",
            "created_at",
            "text",
            "images",
            "child"
        )
