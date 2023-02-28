from .models import Student, Classroom, Professor

from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields= '__all__'
       
class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        

class ProfessorSerializer(ModelSerializer): 
    class Meta:
        model = Professor
        fields = '__all__'