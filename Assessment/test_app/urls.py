from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseTypeView, ModuleView, ModuleUpdateView, ModulePositionView

router = DefaultRouter()
router.register('module', ModuleView)
router.register('dragdrop', ModulePositionView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('course', CourseTypeView.as_view()),
    path('course/<id>', CourseTypeView.as_view()),
    path('module/<id>', ModuleUpdateView.as_view()),
    # path('<pk>/course_delete/', CourseSoftDeleteView.as_view()),
]
