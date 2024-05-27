from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
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
       
        return redirect("/home/")
   
    querySet=Reciepy.objects.all()
    if request.GET.get("search"):
        print(request.GET.get('search'))
        querySet=querySet.filter(receipy_name__icontains=request.GET.get('search'))

    context={"receipes":querySet}   
    return render(request,"index.html",context)

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
        return redirect("/home")
    context={"receipes":queryset}
    print(queryset)
    return render(request,"updteReciepe.html",context)

# delete route
def delete_receipe(request,id):
    queryset=Reciepy.objects.get(id=id)
    queryset.delete()
    return redirect("/home/")

