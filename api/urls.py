from django.urls import path, include
from .views import ClassroomViewSet, StudentViewSet, ProfessorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'students', StudentViewSet)
router.register(r'professors', ProfessorViewSet)

urlpatterns = [
    #path('classroom/post', views.insertClassroom, name='createClassroom'),
    #path('classroom/getAll', views.getClassrooms, name='getAllClassrooms'),
    #path('classroom/delete/<str:pk>', views.deleteClassroom, name='deleteClassroom')

    path('', include(router.urls)),
]