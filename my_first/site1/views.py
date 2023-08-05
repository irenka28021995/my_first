from django.shortcuts import render,redirect
from django.http import HttpResponse
from. models import Molel3,Molel4,Molel5
from. import models,form
from.form import Molel3Form
from django.views.generic import DetailView



def index(request):
  molels = Molel3.objects.all()
  return render(request,"site1/base.html", {"molels":molels})
def about(request):
    molels = Molel5.objects.all()
    return render(request,"site1/about.html", {"molels": molels})

def create(request):
    error=''
    if request.method =='POST':
        form = Molel3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error= 'Форма была неверной'
    form = Molel3Form()
    data={
        'form':form,
        'error':error
          }
    return render(request,"site1/create.html",data)

def news(request):
    molels = Molel4.objects.all()
    return render(request,"site1/news.html",{'molels':molels})

