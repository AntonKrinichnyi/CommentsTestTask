import os
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

UserModel = get_user_model()

def image_file_path(instance, filename):
    _, extencion = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extencion}"
    return os.path.join("uploads/images", filename)

class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    record = models.ForeignKey(
        "comment.CommentModel",
        related_name="child",
        related_query_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(
        null=True,
        blank=True,
        upload_to=image_file_path
    )

    class Meta:
        ordering = ("-created_at", )
