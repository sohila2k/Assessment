from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .utils import COURSE_DELETED

from .models import Course, Module
from .serializers import CourseSerializer, ModuleSerializer


class CourseTypeView(APIView):
    def delete(self, request, id=None):
        try:
            course_meta = Course.objects.get(id=id)
            course_meta.status = COURSE_DELETED
            course_meta.save()
            return Response({"detail": "Case Deleted Successfully"}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({"detail": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        if id:
            item = Course.objects.get(id=id)
            serializer = CourseSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Course.objects.exclude(status=COURSE_DELETED)
        serializer = CourseSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Course.objects.get(id=id)
        serializer = CourseSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


class ModuleView(ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.filter(parent_id=None)


class ModuleUpdateView(APIView):
    def patch(self, request, id=None):
        item = Module.objects.get(id=id)
        serializer = ModuleSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


# class DragAndDRopView(viewsets.ModelViewSet):
#     queryset = Module.objects.all
#     serializer_class = ModuleSerializer

@api_view(['GET', 'PUT'])
def create_module(request, self=None):
    serializer = ModuleSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        last_position = Module.objects.order_by('-position').first()
        if last_position:
            new_position = last_position.position + 1
        else:
            new_position = 1
            name = request.data.get('name')
            description = request.data.get('description')
            position = new_position

            module_instance = Module.objects.create(
                name=name,
                description=description,
                position=position,
            )

            response = {
                "id": module_instance.id,
                "name": module_instance.name,
                "description": module_instance.description,

            }

            return Response(response, status.HTTP_200_OK)
# Create your views here.
