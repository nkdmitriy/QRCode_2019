from django.db import models


#Класс Lector не нужен, будет авторизация и добавление в таблицу auth_user
#class Lector(models.Model):
#    name = models.CharField(max_length=50)
class Group(models.Model):
    name = models.CharField(max_length=30)

	
class Lection(models.Model):
    name = models.CharField(max_length=50)
    lector = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    #lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=50)
    read_date = models.DateTimeField()

	
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

	
class StudentsList(models.Model):
    lection = models.ForeignKey(Lection, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exists = models.BooleanField(default='false')