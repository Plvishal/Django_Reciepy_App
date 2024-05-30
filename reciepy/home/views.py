from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def add_receipe(request):
    if request.method== "POST" :
        data=request.POST
        receipy_img=request.FILES.get("receipy_img")
        receipy_name=data.get("receipy_name")
        receipy_des=data.get("receipy_des")
        Reciepy.objects.create(
            receipy_img=receipy_img,
            receipy_name=receipy_name,
            receipy_des=receipy_des
        )
       
        return redirect("/")
   
    querySet=Reciepy.objects.all()
    # if request.GET.get("search"):
    #     print(request.GET.get('search'))
    #     querySet=querySet.filter(receipy_name__icontains=request.GET.get('search'))

    context={"receipes":querySet}   
    return render(request,"index.html",context)

def detail_by(request,id):
    print(id)
    querySet=Reciepy.objects.get(id=id)
    context={"receipes":querySet}  
    return render(request,"detailBy.html",context)
# Return all Reciepe Card
def home(request):
    querySet=Reciepy.objects.all()
    if request.GET.get("search"):
        print(request.GET.get('search'))
        querySet=querySet.filter(receipy_name__icontains=request.GET.get('search'))
    context={"receipes":querySet} 
    return render(request,"home.html",context)

# update route
def update_receipe(request,id):
    queryset=Reciepy.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipy_img=request.FILES.get("receipy_img")
        receipy_name=data.get("receipy_name")
        receipy_des=data.get("receipy_des")

        queryset.receipy_name=receipy_name
        queryset.receipy_des=receipy_des
        if receipy_img:
            queryset.receipy_img=receipy_img
        queryset.save()
        return redirect("/")
    context={"receipes":queryset}
    print(queryset)
    return render(request,"updteReciepe.html",context)

# delete route
def delete_receipe(request,id):
    queryset=Reciepy.objects.get(id=id)
    queryset.delete()
    return redirect("/")
# Login
def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

