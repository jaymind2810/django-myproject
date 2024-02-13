from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
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

    # Login Check For Master User
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = "You are not alloweded."
        return render(request,'back/error.html', {'error': error})


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


def user_groups_show(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.username)
    groups_list = []
    for i in user.groups.all():
        groups_list.append(i.name)
        print(i.name)

    all_groups = Group.objects.all()

    print(groups_list, "----------groups_list-------")

    return render(request,'back/user-groups.html', {'groups_list': groups_list, 'all_groups': all_groups, 'pk': pk })

def add_user_to_groups(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End
    if request.method == 'POST':
        print("In Post-------Section---------")
        gname = request.POST.get('gname')
        group = Group.objects.get(name=gname)

        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)
        user.groups.add(group)
        print("done----------", pk)
        return redirect('user_groups_show', pk=pk)
    
    if pk:
        print(pk, "-----------In Pk section-------")
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)
        groups_list = []
        for i in user.groups.all():
            groups_list.append(i.name)
            print(i.name)

        all_groups = Group.objects.all()
        return render(request, 'back/user-group-add.html', {'all_groups': all_groups, 'pk': pk})
    

def delete_user_from_groups(request, pk, name):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    try:
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)
        group = Group.objects.get(name=name)
        user.groups.remove(group)
        if pk:
            return redirect('user_groups_show', pk)
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})
    

def manager_perms(request):

    # Login Check For Master User
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = "You are not alloweded."
        return render(request,'back/error.html', {'error': error})


    # Login Check End

    perms = Permission.objects.all()
    print(perms, "============Permisssionfooooooof--------")

    return render(request, 'back/manager_perms.html', {'perms': perms})

def manager_perms_del(request, name):
    
    # Login Check For Master User
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        error = "You are not alloweded."
        return render(request,'back/error.html', {'error': error})


    # Login Check End
    perms = Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_perms')

def manager_perms_create(request):

    print("Herer--------In Create Perms functiona ------------")

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        print("Herssssssrrrrr")
        name = request.POST.get('name')
        codename = request.POST.get('codename')

        if codename == "":
            print("All Fields are required.")
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        if len(Permission.objects.filter(codename=codename)) != 0:
            error = "You entered same code Permssion."
            return render(request,'back/error.html', {'error': error})
        

        content_type = ContentType.objects.get(app_label='main', model='main')
        print(content_type, "--------ContentType-------------")
        permission = Permission.objects.create(codename=codename, name=name, content_type=content_type)

        # permission.save()
        return redirect('manager_perms')

    return render(request, 'back/manager_perms_create.html', {})
    
    
