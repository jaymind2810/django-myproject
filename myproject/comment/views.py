from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from main.models import Main
from product.models import Product
from manager.models import Manager
from django.core.files.storage import FileSystemStorage
import datetime
import random
# Create your views here.


def product_comment_add(request, pk):
    print("Herereooooooo kdfjkj")

    if request.method == 'POST':

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day

        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)


        title = request.POST.get('title')
        cm = request.POST.get('comment')

        if request.user.is_authenticated :
            print("-------__here----------")
            manager = Manager.objects.get(username=request.user)
            print(manager, "---------Manager--------")

            b = Comment(
                name=manager.username, 
                email=manager.email, 
                product_id=pk, 
                title=title, 
                description=cm, 
                date=today, 
                time=time)
            print(b, "=========B =========")
            b.save()
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment(
                name=name, 
                email=email, 
                product_id=pk, 
                title=title, 
                description=cm, 
                date=today, 
                time=time)
            print(b, "-----------B-------")
            b.save()

    return redirect('product_details', pk)


def product_comment_delete(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        a = Comment.objects.get(pk=pk).name
        if str(a) != str(request.user) :
            error = "Access Denied."
            return render(request,'back/error.html', {'error': error})
        
    p = Comment.objects.filter(pk=pk)
    product = Product.objects.get(int(p.product_id))

    try:
        p.delete()
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})

    return redirect('product_details', product)

