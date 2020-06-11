from django.shortcuts import render,redirect    # redirect'i sonradan dahil ettik.
from .forms import RegisterForm, LoginForm # forms.py'den RegisterForm class'ını çağırdık.
from django.contrib.auth.models import User # User kullanıcımızı dahil ettik.
from django.contrib.auth import login, authenticate,logout   # User'ımızın login olması için bu modulü dahil ettik. Çıkış yapmak için de logout'u dahil ettik.
from django.contrib import messages # Yayınlamak istediğimiz mesaj çeşitlerini buradan alıyoruz.
#from django.contrib.auth import authenticate    # Database'de sorgu yapmak için kullanıyoruz. Kullanıcıdan alınan username ve password'ü kontrol edecek.

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid(): # clean methodunun çalışması için bu fonksiyonu kullanmalıyız.
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)  # password'ün şifrelenmesi için set_password kullandık.
        newUser.save()  # Veritabanına kaydetme
        login(request,newUser)
        messages.info(request,"Kayıt işlemi başarılı")  # info özelliğini layout'ta koşullu durumla danger yaptık.

        return redirect("index") # login olduktan sonra anasayfaya yönelmesi için gitmesini istediğimiz url'in ismini verdik.
    context = {
        "form" : form
        }
    return render(request,"register.html",context)

    """ 2. Yol
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): # clean methodunun çalışması için bu fonksiyonu kullanmalıyız.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)  # password'ün şifrelenmesi için set_password kullandık.
            newUser.save()  # Veritabanına kaydetme
            login(request,newUser)

            return redirect("index") # login olduktan sonra anasayfaya yönelmesi için gitmesini istediğimiz url'in ismini verdik.
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)"""


    """
    1. Yol
    form = RegisterForm()   # class'ımızı form'a eşitledik.
    context = {
        "form" : form
    }   # Ardından bu form'u çağırabilmek için sözlük tipinde yazdık.
    return render(request,"register.html",context)"""  # En sonunda register.html'de döndürebilmek için context'i buraya dahil ettik.

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya şifre hatalı")    # danger'ı kullanmak için info yaptık
            return render(request,"login.html",context)
        messages.success(request,"Giriş Başarılı")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Başarılı")
    return redirect("index")