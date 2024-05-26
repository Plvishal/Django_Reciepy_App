from django.shortcuts import render, redirect
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
    return render(request,"index.html")
