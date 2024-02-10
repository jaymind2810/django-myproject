from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from .models import Category
import datetime
# Create your views here.


def category_list(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    # site = Main.objects.get(pk=2)
    categories = Category.objects.all()

    return render(request, 'back/categories-list.html', {'categories': categories})

def category_create(request):
    print("hjhfjsfjdhsjfhdj")

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    if request.method == 'POST':
        print("Herssssssrrrrr")
        category_name = request.POST.get('name')
        description = request.POST.get('description')

        if category_name == "" or description == "":
            print("All Fields are required.")
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        if len(Category.objects.filter(name=category_name)) != 0:
            error = "You entered same name Category."
            return render(request,'back/error.html', {'error': error})
                
        b = Category(name=category_name, description=description)
        b.save()
        return redirect('category_list')

    return render(request, 'back/categories-create.html', {})

def category_delete(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    try:
        p = Category.objects.filter(pk=pk)
        p.delete()
        return redirect(category_list)
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})

    

