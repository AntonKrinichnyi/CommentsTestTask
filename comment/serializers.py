from django.contrib.auth import get_user_model
from rest_framework import serializers

from comment.models import CommentModel

User = get_user_model()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username"
        )


class RecordSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(read_only=True)

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "user_info",
            "text",
            "created_at",
            "image"
        )


class CommentSerializer(serializers.ModelSerializer):
    single_record = RecordSerializer(many=True, read_only=True)
    user_info = UserInfoSerializer(read_only=True)

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "user_info",
            "created_at",
            "text",
            "single_record",
            "image"
        )
