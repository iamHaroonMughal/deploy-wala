from django.shortcuts import render , HttpResponse , redirect
from .models import *
# Create your views here.

def index(request):
    if request.method =='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        address = data.get("address")
        phone = data.get("phone")
        
        Employees.objects.create(
        name =  name ,
        email = email,
        address = address,
        phone = phone
        )
        return redirect("/")
    
    
    queryset = Employees.objects.all()
    context = {"entries": queryset}
        
        
    
        
    return render(request , 'index.html' , context)


def update(request , id ):
    if request.method =='POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        address = data.get("address")
        phone = data.get("phone")
        
        emp = Employees(
        id = id,
        name =  name ,
        email = email,
        address = address,
        phone = phone
        )
        
        emp.save()
        return redirect('/')
    
    

    return redirect(request , "index.html" )





def delete(request , id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    
    context = {
        'entries' : emp
    }
    
    return redirect('/')
    
    return redirect(request , "index.html" , context)



