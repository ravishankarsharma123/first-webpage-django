from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable":"any think"
    }
    messages.success(request, "This is a text messages")
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        descc=request.POST.get('descc')
        contact=Contact(name=name,email=email,descc=descc,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    
    return render(request, 'contact.html')
  
   
