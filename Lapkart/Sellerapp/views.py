from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop


def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/seller/show/")
    template_name = "Sellerapp/add_laptop.html"
    form = LaptopForm()
    context = {"form":form}
    return render(request,template_name,context)
@login_required(login_url="/auth/login/")
def show_laptop(request):
    template_name = "Sellerapp/show_laptops.html"
    laptop_objs = Laptop.objects.all()
    context = {"laptop_objs":laptop_objs}
    return render(request,template_name,context)

def update_laptop(request,i):
    lap_obj = Laptop.objects.get(id=i)
    if request.method == "POST":
        form = LaptopForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect("/seller/show/")
    template_name = "sellerapp/add_laptop.html"
    form = LaptopForm(instance=lap_obj)
    context = {"form":form}
    return render(request,template_name,context)

def delete_laptop(request,j):
    lap_obj=Laptop.objects.get(id=j)
    lap_obj.delete()
    return redirect("/seller/show/")





