from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
    #获取后台数据
    posts=Posts.objects.all()
    context={
        'title':"this is latest posts",
        'posts':posts
    }
    return render(request,'blogs/index.html',context)

def details(request,id):
    post=Posts.objects.get(id=id)
    context={
        "post":post
    }
    return render(request,'blogs/details.html',context)