from rest_framework.serializers import ModelSerializer
from .models import Course, Module


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'description', 'image', 'status']


class ModuleSerializer(ModelSerializer):
    course_create = CourseSerializer(read_only=True, many=True)

    def to_representation(self, instance):
        parent_id = instance.id
        queryset = Module.objects.filter(parent_id=parent_id)
        children = 'end statement'

        if queryset.exists():
            children = ModuleSerializer(instance.children, many=True, read_only=True).data
        response = super().to_representation(instance)
        response['children'] = children
        return response

    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'parent_id', 'course_id', 'course_create', 'position']
