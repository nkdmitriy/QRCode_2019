from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import LectionForm, Lection, Student, StudentsList
from django.contrib.auth.models import User
from django.views import generic
from .forms import ValidPhoneForm

class StudentListView(generic.ListView):
    template_name = 'studentslist.html'
    context_object_name = 'liststudents'
 
    def get_queryset(self):
        return Student.objects.filter(group=1)
	#def get_queryset(self, group_id):
        #return Student.objects.filter(group=group_id)

	
def create_lection(request, lection_id):
    return HttpResponse("Number created lection - " + str(lection_id))
	#Генерация QR кода
	
def lection_studentslist(request, lection_id):
    lection = lection_id
    list = StudentsList.objects.filter(lection=lection_id).values_list('id', flat=True)
    liststudents = Student.objects.filter(studentslist__in=list, studentslist__exists=False).order_by('surname')
    #return HttpResponse(lists)
    return render(request, 'students.html', {'liststudents': liststudents, 'lection':lection})
	

# class StudentsView(gener	ic.ListView):
    # template_name = 'students.html'
    # context_object_name = 'liststudents'
 
    # def get_queryset(self):
        # return StudentsList.objects.filter(lection=lection_id)

def qrcode(request):
    if request.method == 'POST':
        form = LectionForm(request.POST)
        if form.is_valid():
		#data = {'name': 'Python. Part 2', 'group': 'IB1', 'read_date': '2019-07-08 07:54:48.000000', 'lector': '2', 'qrcode': 'URL'}
            name = form.cleaned_data['name']
            group = form.cleaned_data['group']
            read_date = form.cleaned_data['read_date']
            new_lection = Lection(name=name, lector=User.objects.get(id=2), group=group, qrcode='URL', read_date=read_date)
            st_list = Student.objects.filter(group__name__exact=group)
            new_lection.save()
            for i in range(0, len(st_list)):
			#возможно добавлять в список, чтобы обращение к БД при сохранении происходило 1 раз
                student_on_lection = StudentsList(lection=new_lection, student=st_list[i])
                student_on_lection.save()
            urls = '/QR/lection/'+str(new_lection.id)+'/studentslist'
            return HttpResponseRedirect(urls)
    else:
        form = LectionForm()

    return render(request, 'name.html', {'form': form})
	
def validphone(request, lection_id, student_id):
    validphoneform = ValidPhoneForm()
    #return render(request, "validation.html", {"form": validphoneform})
	
	
    if request.method == 'POST':
        form = ValidPhoneForm(request.POST)
        #if not form['phone']:
         #   errors.append('Формат номера - 10 цифр')
             
        if form.is_valid():
            # ... сохранение данных в базу
            #new_lection = Lection.objects.filter(lection__id=lection_id)
            phone = form.cleaned_data['phone']
            #currentphone = Student.objects.filter(id__exact=student_id).values('phone')
            valid = StudentsList.objects.filter(student__phone=phone, lection_id=lection_id).update(exists=True)
            if valid == 1:
                return HttpResponse('Личность подтверждена. Спасибо.')
            else:
                return HttpResponse('Ошибка подтверждения личности. Введенный номер не соответствует занесенному в БД.')
    student = Student.objects.filter(id=student_id).values_list('firstname', 'phone')
    #Для ускорения тестирования временно выведим телефон студента на форму
    return render(request, 'validation.html', {'form':validphoneform, 'firstname':student[0][0], 'phone':student[0][1]})
