from django.shortcuts import render
from .forms import StudentRegistration


def index(request):
    return render(request, 'main/index.html')


def student_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)   
        if fm.is_valid():
            fm.save() 
    else:
        fm = StudentRegistration()
    
    return render(request, 'main/student_form.html', {'form':fm})