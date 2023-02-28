from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Student, Classroom, Professor
from .serializers import StudentSerializer, ClassroomSerializer, ProfessorSerializer

@api_view(['GET'])
def getClassrooms(request):
    classrooms = Classroom.objects.all()
    classrooms_serializer = ClassroomSerializer(classrooms, many=True)
    return JsonResponse(classrooms_serializer.data, safe=False)

@api_view(['POST'])
def insertClassroom(request):
    classroom_data = Classroom.objects.create()
    classroom_data.nbr_students = 0
    classroom_data.math_mean_note = 0
    classroom_data.german_mean_note = 0
    classroom_data.portuguese_mean_note = 0
    classroom_data.professors.set([]) 
    classroom_serializer = ClassroomSerializer(data=classroom_data)
    if classroom_serializer.is_valid():
        classroom_serializer.save()
        return JsonResponse(classroom_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(classroom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteClassroom(request, pk):
    classroom = Classroom.objects.get(id=pk)
    if request.method == 'DELETE':
        classroom.delete()
        return JsonResponse({'message': 'Classroom was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)