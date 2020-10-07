from django.shortcuts import render 
from .models import Employee
  
def index_view(request): 
    return render(request, "index.html")

def employee_view(request):
    employees = Employee.objects.all

    return render(request, "pekerja.html", {'employees':employees})  
