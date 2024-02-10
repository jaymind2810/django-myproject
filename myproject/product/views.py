from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.


def product_details(request, pk):

    site = Main.objects.get(pk=2)
    products = Product.objects.filter(pk=pk)

    return render(request, 'front/product_details.html', {'site': site, 'products': products})



def product_list(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    # site = Main.objects.get(pk=2)
    products = Product.objects.all()

    return render(request, 'back/product-list.html', {'products': products})


def product_create(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

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

    # site = Main.objects.get(pk=2)
    if request.method == 'POST':
        print("Herrrrrr")
        product_name = request.POST.get('product_name')
        short_text = request.POST.get('short_text')
        amount = request.POST.get('amount')

        if product_name == "" or short_text == "" or amount == "":
            print("All Fields are required.")
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        print(request.FILES, "ppppppppppppppsakdj")

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):
                if myfile.size < 5000000:
                    b = Product(name=product_name, short_text=short_text, amount=amount, description="--", picname =filename, picurl=url, date=today, time=time)
                    b.save()
                    return redirect('product_list')
                else:
                    error = "Your File is Too Large."
                    return render(request,'back/error.html', {'error': error})

            else:
                error = "Your File is not Supported."
                return render(request,'back/error.html', {'error': error})
        except:
            error = "Please Input image file."
            return render(request,'back/error.html', {'error': error})

    return render(request, 'back/product-create.html', {})

def product_edit(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    # site = Main.objects.get(pk=2)
    if len(Product.objects.filter(pk=pk)) == 0:
        error = "Product Not Found."
        return render(request,'back/error.html', {'error': error})
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        print("Herrrrrr")
        product_name = request.POST.get('product_name')
        short_text = request.POST.get('short_text')
        amount = request.POST.get('amount')

        if product_name == "" or short_text == "" or amount == "":
            print("All Fields are required.")
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        print(request.FILES, " -------In Edit--------")

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):
                if myfile.size < 5000000:
                    b = Product.objects.get(pk=pk)

                    fsold = FileSystemStorage()
                    filename1 = fsold.delete(b.picname)

                    b.name = product_name
                    b.short_text = short_text
                    b.amount = amount
                    b.picname = filename
                    b.picurl = url
                    b.save()
                    return redirect('product_list')
                else:
                    error = "Your File is Too Large."
                    return render(request,'back/error.html', {'error': error})

            else:
                error = "Your File is not Supported."
                return render(request,'back/error.html', {'error': error})
        except:
            error = "Please Input image file."
            return render(request,'back/error.html', {'error': error})



    return render(request, 'back/product-edit.html', {'product': product})

def product_delete(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    try:
        p = Product.objects.filter(pk=pk)

        # print(p.picname, "---------pic Name ")
        # if p.picname:
        #     fs = FileSystemStorage
        #     fs.delete(p.picname)

        p.delete()
    except:
        error = "Something went Wrong."
        return render(request,'back/error.html', {'error': error})

    return redirect(product_list)