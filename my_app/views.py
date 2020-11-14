from django.shortcuts import render,HttpResponse,redirect

from .forms import *

# Create your views here.
from .models import Friends,Products 
def show_friends(request):
    friend=Friends.objects.all()
    context={'friends':friend}
    return render(request,'my_app/friends.html',context)

def show_products(request):
    product=Products.objects.all()
    context={'products':product}
    return render(request,'my_app/products.html',context)    

def product_details(request,id):
    p=Products.objects.get(id=id)
    context={'product':p}
    return render(request,'my_app/product_details.html',context)

def add_product(request):
    if request.method=='POST':
        form=ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Successfully Done")
            return redirect('/products')
    form=ProductsForm()
    context={'form':form}
    return render(request,'my_app/add_product.html',context)

def user_creation_form(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        password= request.POST.get('password')
        username= request.POST.get('username')
        print(password)
        if form.is_valid():
            user=User.objects.create_user(username=username, password=password)
            return HttpResponse("Successfully Signed Up")
    form = UserForm()
    context={'form':form}
    return render(request,'my_app/singup.html',context)