from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import Student


def index(request):
    return render(request, 'main/index.html')


def student_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)   
        if fm.is_valid():
            f_name = fm.cleaned_data['first_name']
            l_name = fm.cleaned_data['last_name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            entity = Student(first_name=f_name, last_name=l_name, email=email, phone=phone)
            entity.save() 
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    student = Student.objects.all()
    
    print(len(student))
    
    return render(request, 'main/student_form.html', {'form':fm, 'student':student})