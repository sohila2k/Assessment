import uuid
from datetime import timezone

from django.db import models
from .validators import validate_image_extension


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True, validators=[validate_image_extension])
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Module(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField()
    course_id = models.ForeignKey(Course, related_name='course_create', on_delete=models.SET_NULL,null=True)
    parent_id = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
# Create your models here.
