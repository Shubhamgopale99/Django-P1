from django.shortcuts import render
from.models import users

def index(request):
    U = users.objects.all()
    return render (request,'index.html',{'users': U})
# Create your views here.
