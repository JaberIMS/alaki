from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    my_dic = {'insert_me123':"Now I am from first_app/index.html!"}
    return render(request,'first_app/index.html',context=my_dic)
