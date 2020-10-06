from django.shortcuts import render 
  
def index_view(request): 
    return render(request, "index.html")

def employee_view(request):


    return render(request, "pekerja.html")  
