from django.db import models
from django.forms import ModelForm


#Класс Lector не нужен, будет авторизация и добавление в таблицу auth_user
#class Lector(models.Model):
#    name = models.CharField(max_length=50)
class Group(models.Model):
    name = models.CharField(max_length=30)
	
    def __str__(self):
        return self.name

	
class Lection(models.Model):
    name = models.CharField(max_length=50)
    lector = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    #lector = models.IntegerField(default='0')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=50)
    read_date = models.DateTimeField()
	
    def __str__(self):
        return self.name

	
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
	
    def __str__(self):
        return self.surname# + ' ' + self.firstname + ' ' + self.patronymic

	
class StudentsList(models.Model):
    lection = models.ForeignKey(Lection, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exists = models.BooleanField(default=False)
	

class LectionForm(ModelForm):
    class Meta:
        model = Lection
        exclude = ['qrcode', 'lector']