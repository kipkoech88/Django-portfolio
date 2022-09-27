from django.shortcuts import render
from django.http import HttpResponse 
from land.forms import UserForm

# Create your views here.
def index(request):
    return render(request, "land/index.html") 

def about(request):
    return render(request, 'land/about.html') 

def services(request):
    return render(request, 'land/services.html') 

def contact_us(request):
    return render(request, 'land/contact.html') 

def sign_up(request): 
    form=UserForm() 
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True) 
            return index(request) 
        else:
            print(form.errors) 
    return render(request, 'land/sign.html', {'form':form})

    return render(request, "land/sign.html") 
