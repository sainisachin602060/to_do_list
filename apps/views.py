from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import login

# Create your views here.

def home(request):
    return render(request,'home.html')


def save(request):
    if request.method=='POST':
        date=request.POST['date']
        goal1=request.POST['goal1']
        goal2=request.POST['goal2']
        login(date=date,goal1=goal1,goal2=goal2).save()
        msg="Goal has been saved✔️"
        return render(request,'home.html',{'msg':msg})
        
    else:
        return HttpResponse("eroro 404")     
    
def show(request):
    data=login.objects.all()
    return render(request,'show.html',{'data':data})

def delete(request):
    date=request.GET['date']
    login.objects.filter(date=date).delete()
    return HttpResponseRedirect('/show/')


def edit(request):
    date=request.GET['date']
    data1=login.objects.filter(date=date)
    return render(request,'edit.html',{'data1':data1})
    
def edited(request):
    if request.method=='POST':
        date=request.POST['date']
        goal1=request.POST['goal1']
        goal2=request.POST['goal2']
        login.objects.filter(date=date).update(goal1=goal1,goal2=goal2)
        return HttpResponseRedirect('/show/')
        
    
    else:
        return HttpResponse("erorr404")
            