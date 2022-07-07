from datetime import datetime
from email import message
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "Hi GUYS"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is HOME page . . .")

def feature(request):
    return render(request,'feature.html')
    # return HttpResponse("This is ABOUT page . . .")
    
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is ABOUT page . . .")
    
def blog(request):
    return render(request,'blog.html')
    # return HttpResponse("This is BLOG page . . .")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, desc=desc, query=query, date=datetime.today())
        contact.save()
        messages.success(request, 'Contact request submitted successfully.')

    return render(request,'contact.html')
    # return HttpResponse("This is CONTACT page . . .")