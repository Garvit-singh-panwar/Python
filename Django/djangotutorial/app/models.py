from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    ALL_SUBJECT = [
        ('Math' , "Mathmatics" ),
        ('Py' , "Python"),
        ("cpp" ,"C_Plus_Plus"),
        ("JS" , "Javascript"),
        ("DJ" , "Django"),
        ("CS" , "CyberSecurity"),
        ("DS" , "DataScience"),
        ('CC' , "CloudComputing"),
    ]

    CHOOSE_SEMSETER = [
        ('I' , "1st SEM"),
        ("II" , "2nd SEM"),
        ("III" , "3rd SEM"),
        ("IV" , "4th SEM"),
        ("V" , "5th SEM"),
        ("VI" , "6th SEM"),
    ] 
    StudentName = models.CharField(max_length=100)
    data_added = models.DateTimeField(default=timezone.now())
    studentImage = models.ImageField(upload_to="Students/")
    Sem = models.CharField(max_length=3 , choices= CHOOSE_SEMSETER)
    sub = models.CharField(max_length=4 , choices=ALL_SUBJECT)

    def __str__(self):
        return self.StudentName
    

