from django.db import models

class Professor(models.Model): 
    name = models.CharField(max_length=200)
    salary = models.FloatField(null=True)

    def __str__(self):
        return str(self.name) 

class Classroom(models.Model):
    nbr_students = models.IntegerField(null=True)
    german_mean_note = models.FloatField(null=True)
    math_mean_note = models.FloatField(null=True)
    portuguese_mean_note = models.FloatField(null=True)
    professors = models.ManyToManyField(Professor, related_name='professors', blank=True)

    def __str__(self):
        return str(self.id) 

class Student(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.SET_NULL)
    frequency = models.FloatField(null=True)
    german = models.FloatField(null=True)
    mathematics = models.FloatField(null=True)
    portuguese = models.FloatField(null=True)

    def __str__(self):
        return str(self.name) 
    

