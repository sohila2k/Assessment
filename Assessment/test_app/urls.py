from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseTypeView, ModuleView, ModuleUpdateView,create_module

router = DefaultRouter()
router.register('module', ModuleView)
# router.register('dragdrop', DragAndDRopView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('course', CourseTypeView.as_view()),
    path('course/<id>', CourseTypeView.as_view()),
    path('module/<id>', ModuleUpdateView.as_view()),
    path('create_module', create_module),
    path('create_module/<id>', create_module),
    # path('<pk>/course_delete/', CourseSoftDeleteView.as_view()),
]
