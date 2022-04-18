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
            record = Student(first_name=f_name, last_name=l_name, email=email, phone=phone)
            record.save() 
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    students = Student.objects.all()
    return render(request, 'main/student_form.html', {'form':fm, 'students':students})


def update_data(request, id):
    if request.method== 'POST':
        record = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=record) # Generating a form with the values of the record with the given id
        if fm.is_valid():
            fm.save()
    else:
        record = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=record) 
    return render(request, 'main/update_data.html', {'form':fm})


def delete_data(request, id):
    if request.method == 'POST':
        record = Student.objects.get(pk=id) 
        record.delete()
        return redirect('/main/student_form')