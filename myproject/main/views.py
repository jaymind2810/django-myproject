from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from product.models import Product
from manager.models import Manager
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):

    site = Main.objects.get(pk=2)
    products = Product.objects.all()

    return render(request, 'front/home.html', {'site': site, 'products': products})

def about(request):
    site = Main.objects.get(pk=2)

    return render(request, 'front/about-us.html',{'site': site})


def panel(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    site = Main.objects.get(pk=2)
    products = Product.objects.all()

    return render(request, 'back/home.html', {'site': site, 'products': products})

def mylogin(request):

    if request.method == 'POST':

        utext = request.POST.get('username')
        ptext = request.POST.get('password')

        if utext != "" and ptext != "":
            user = authenticate(username=utext, password=ptext)

            if user != None:

                login(request, user)
                return redirect('home') 

    return render(request, 'front/login.html')

def myregister(request):

    if request.method == 'POST':

        uemail = request.POST.get('useremail')
        utext = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error = "Password didn't match."
            return render(request,'back/error.html', {'error': error})
        
        if len(User.objects.filter(username=utext)) == 0 and len(User.objects.filter(email=uemail)) == 0:
            print("Here-------------")
            ip, ip_routable = get_client_ip(request)
            print(ip, "------Ip-----------")
            if ip is None:
                ip = "0.0.0.0"

            try:
                response = DbIpCity.get(ip, api_key="free")
                country = response.country + " | " + response.city
            except:
                country = "UnKnown"
            
            user = User.objects.create_user(username=utext, email=uemail, password=password1)
            print(user, "======user")
            manager = Manager(username=utext, email=uemail, name=utext, ip=ip, country=country)
            manager.save()

            print("Before Mail000000000000000000000000000")

            to_email = uemail
            subject = "Account Created."
            message = "Your Account Success Fully Created."
            email_from = settings.EMAIL_HOST_USER
            emails = [to_email]
            
            send_mail(subject, message, email_from, emails)

            # send_mail(
            #     'Subject Here Second Way',
            #     message,
            #     'sender@gmail.com',
            #     [to_email],
            #     fail_silently=False
            # )
            print("After Mail ==========================")

            return redirect(mylogin)

    return render(request, 'front/register.html')

def mylogout(request):

    logout(request)
    return redirect(mylogin)

def change_password(request):

    if request.method == "POST":

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        print(oldpass, newpass, "---------Old AND New")

        if oldpass == "" and newpass == "":
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        
        user = authenticate(username=request.user, password=oldpass)

        if user != None:
            print("Okokokokok")
            user = User.objects.get(username=request.user)
            user.set_password(newpass)
            user.save()
            return redirect('mylogout')

        else:
            error = "Your password Is Not currected."
            return render(request,'back/error.html', {'error': error})

    

    return render(request, 'back/password-reset.html')

def site_setting(request):
    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    site = Main.objects.get(pk=2)

    if request.method== "POST":
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        about = request.POST.get('about')
        link = request.POST.get('link')
        email = request.POST.get('email')
        location = request.POST.get('location')

        if link == "": link = "#"

        if name == "" or tell == "":
            error = "All Fields are required."
            return render(request,'back/error.html', {'error': error})
        
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            b = Main.objects.get(pk=2)
            b.set_name = name
            b.tell = tell
            b.about = about
            b.link = link
            b.email = email
            b.picname = filename
            b.picurl = url
            b.location = location
            b.save()

        except:
            b = Main.objects.get(pk=2)
            b.set_name = name
            b.tell = tell
            b.about = about
            b.link = link
            b.email = email
            b.location = location
            b.save()


    return render(request, 'back/setting.html', {'site': site})


