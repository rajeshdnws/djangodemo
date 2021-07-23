from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
def home_view(request,*args,**kwargs):
   # return HttpResponse("Hello, world. You're at the home index.")
   return render(request,"home.html",{})
def contact_view(request,*args,**kwargs):
   if request.method=="POST":
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    pwd=request.POST['pwd']
    phone=request.POST['phone']
    condition=request.POST['condition']
    if condition=='on':
        cond=1
    else:
        cond=0
    ins =Contact(fname=fname,lname=lname,email=email,pwd=pwd,phone=phone,condition=cond)
    ins.save()
         
   return render(request,"contact.html")

def  about_view(request,*args,**kwarg):
    #return HttpResponse('<h1>helloo about page</h1>')
    return render(request,"aboutus.html",{})
