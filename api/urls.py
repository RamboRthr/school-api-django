from django.urls import path
from . import views

urlpatterns = [
    path('classroom/post', views.insertClassroom, name='createClassroom'),
    path('classroom/getAll', views.getClassrooms, name='getAllClassrooms'),
    path('classroom/delete/<str:pk>', views.deleteClassroom, name='deleteClassroom')
]