from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Contact


def contacts(request):
    if request.method == "POST":
        FirstName= request.POST['firstname']
        LastName= request.POST['lastname']
        Email= request.POST['email']
        ContactNumber= request.POST['phone']
        add = Contact(FirstName= FirstName, LastName= LastName, Email= Email, ContactNumber= ContactNumber)
        add.save()
    Data = Contact.objects.all().values()
    return render(request,"index.html",{'Data':Data})

    
def index(request):
    Data = Contact.objects.all().values()
    return render(request,"index.html",{'Data':Data})

def formupdate(request,id):
        if request.method == "POST":
            add=Contact.objects.get(id=id)
            add.FirstName= request.POST["firstname"]
            add.LastName= request.POST["lastname"]
            add.Email= request.POST["email"]
            add.ContactNumber= request.POST['phone']
            add.save()
            return redirect("index")
        
def edit(request,id):
        Data = Contact.objects.get(id=id)
        return render(request,'edit.html',{'Data':Data})

def delete(request,id):
        add = Contact.objects.get(id=id)
        add.delete()
        return redirect('index')

def search(request):
    query=request.GET["query1"]
    Data=Contact.objects.filter(contactNumber__icontains=query)
    params={'Data':Data}
    return render(request,'search.html',params)
    
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())