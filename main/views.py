from django.shortcuts import render, redirect
from .forms import TeachersForm
from .models import Teacher, Teachers

# Create your views here.

def home(request):
    return render(request, 'schoolsite/home.html')

def reg(request):
    error=''
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teach')
        else:error='Форма заполнена неправильно'

    form = TeachersForm
    data={'form':form,
          'error':error}
    return render(request, 'schoolsite/reg.html', data)

def teacher(request):
    all1=Teachers.objects.all()
    all=Teacher.objects.all()
    return render(request, 'schoolsite/teachers.html', {'all1':all1, 'all':all})