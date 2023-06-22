from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from optparse import Option
from django.contrib import auth
from django.contrib.auth import authenticate
def index(request):
    return render(request, 'index.html')
def index1(request):
    return render(request, 'index1.html')
def faq(request):
    return render(request, 'faq.html')
def drugs(request):
    return render(request, 'drugs.html')
def desc(request):
    return render(request, 'desc.html')
def upload(request):
    return render(request, 'upload.html')
def test(request):
    return render(request, 'Physical test.html')
def doc1(request):
    return render(request, 'doc1.html')
def doc2(request):
    return render(request, 'doc2.html')
def doc3(request):
    return render(request, 'doc3.html')
def call1(request):
    return render(request, 'call1.html')
def call2(request):
    return render(request, 'call2.html')
def call3(request):
    return render(request, 'call3.html')
def loc1(request):
    return render(request, 'loc1.html')
def loc2(request):
    return render(request, 'loc2.html')
def loc3(request):
    return render(request, 'loc3.html')
def signup(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        username=request.POST.get('uname')
        password=request.POST.get('pword')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        user=User.objects.create_user(first_name=Name,username=username,password=password,email=email,)
    
        print('account created')
        return redirect('index.html')
    else:
        return render(request, 'signup.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        psword=request.POST.get('pword')

        user=auth.authenticate(username=uname,password=psword,)
        
        print('logged in')
        return redirect('upload.html')
        
    else:
        return render(request, 'login.html')
# Create your views here.
