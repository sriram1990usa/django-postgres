from django.shortcuts import render
from .models import Teacher

def index(request):
    teachers = Teacher.objects.all()
    return render(request, 'app/index.html', {'teachers':teachers})