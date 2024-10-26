from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def get_all(request):
    tasks = Tasks.objects.all()
    return render(request,"index.html",context={"tasks":tasks})


def get_by_id(request,pk):
    tasks  = Tasks.objects.filter(id=pk).first()
    if tasks:
        return render(request,"index1.html",context={"tasks":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add(request):
    if request.method == "POST":
        form  = Tasksform(request.POST)
        if form .is_valid():
            form.save()
            return redirect("get_all")
    else:
        form = Tasksform()
    return render(request,"index3.html", context={"form":form})



def update(request,pk):
    tasks  = Tasks.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Tasksform(request.POST, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("get_all")
        else:
            form = Tasksform()
        return render(request,"index4.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete(request,pk):
    tasks = Tasks.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("get_all")
        else:
            return render(request,"delete.html",context={"tasks":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
        
    
 
    


