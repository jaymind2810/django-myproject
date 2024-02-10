from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth.models import User, Group, Permission
# Create your views here.


def user_list(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    # site = Main.objects.get(pk=2)
    user_list = Manager.objects.all()

    return render(request, 'back/user-list.html', {'user_list': user_list})

def user_delete(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    try:
        p = Manager.objects.get(pk=pk)
        user = User.objects.filter(username=p.username)
        user.delete()
        p.delete()
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})

    return redirect(user_list)


def manager_group(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    # site = Main.objects.get(pk=2)
    groups_list = Group.objects.all()

    return render(request, 'back/manager_group.html', {'groups_list': groups_list})

def manager_group_create(request):

    print("Herer--------In Create group functiona ------------")

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        print("Herssssssrrrrr")
        name = request.POST.get('name')

        if name == "":
            print("All Fields are required.")
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        if len(Group.objects.filter(name=name)) != 0:
            error = "You entered same name Category."
            return render(request,'back/error.html', {'error': error})
                
        b = Group(name=name)
        b.save()
        return redirect('manager_group')

    return render(request, 'back/manager_group_create.html', {})


def manager_group_delete(request, name):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    try:
        p = Group.objects.filter(name=name)
        p.delete()
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})

    return redirect(manager_group)
