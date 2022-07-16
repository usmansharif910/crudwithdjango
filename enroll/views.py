#from django.http import HttpResponseRedirect
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST or None)
 

  if fm.is_valid():
    nm = fm.cleaned_data['name']
    em = fm.cleaned_data['email']
    pw = fm.cleaned_data['password']
    cm = fm.cleaned_data['comment']
    reg=User (name=nm,email=em, password=pw,comment=cm)
    reg.save()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud}) 
  fm = StopAsyncIteration()
 else:
  fm= StudentRegistration() 

 stud = User.objects.all()
 return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud}) 


#This function will updata record
def update_data(request, id):
  if request.method =='POST':
   pi = User.objects.get(pk=id)
   fm = StudentRegistration(request.POST or None, instance=pi)
  #  fm= StudentRegistration()
  #  return render(request,'enroll/updatestdt.html',{'form':fm, 'id':id})
   if fm.is_valid():
      # nm = fm.cleaned_data['name']
      # em = fm.cleaned_data['email']
      # pw = fm.cleaned_data['password']
      # re=User (name=nm,email=em, password=pw)
      fm.save()
      
  else:
   pi = User.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
  return render(request,'enroll/updatestdt.html',{'form':fm,'id':id})
  

#This function will delete data
def delete_data(request, id):
  if request.method == 'POST':
   pi = User.objects.get(pk=id)
   pi.delete()
  # return HttpResponseRedirect()
  fm= StudentRegistration() 
  stud = User.objects.all()
  return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud}) 
  