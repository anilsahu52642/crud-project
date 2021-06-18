from django.shortcuts import render,HttpResponseRedirect
from .forms import studentform
from .models import student
from django.contrib import messages



def createandshow(request):
    if request.method=='POST':
        stud=studentform(request.POST)
        if stud.is_valid:
            stud.save()
            messages.success(request,'successfully saved record......')
        else:
            messages.error(request,'some data enered is incorrect.....')    
    studdata=student.objects.all()
    stud=studentform
    return render(request,'home1.html',{'form':stud,'studdata':studdata})


def delete(request,pk):
    
    stdata=student.objects.get(id=pk)
    stdata.delete()
    messages.success(request,'data deleted successfully........')
    return HttpResponseRedirect('/create/')


def update(request,id):
    if request.method=='POST':
        studata1=student.objects.get(pk=id)
        studata2=studentform(request.POST,instance=studata1)
        if studata2.is_valid:
            studata2.save()
            messages.success(request,'data updated successfully......')
        stud=studentform
        
    else:
        studata1=student.objects.get(pk=id)
        stud=studentform(instance=studata1)
    studdata=student.objects.all()
    return render(request,'home1.html',{'form':stud,'studdata':studdata})


    