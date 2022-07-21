from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Course, Module
from .serializers import CourseSerializer, ModuleSerializer


class CourseTypeView(APIView):

    def get(self, request, id=None):
        if id:
            item = Course.objects.get(id=id)
            serializer = CourseSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Course.objects.all()
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

    def delete(self, request, id=None):
        try:
            soft_delete = Course.objects.get(id=id)
            soft_delete.save()
            return Response({"detail": "Soft Deleted Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"detail": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


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


class ModulePositionView(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            last_position = Module.objects.order_by('-position').first()
            if last_position:
                new_position = last_position.position + 1
            else:
                new_position = 1

    # Create your views here.
