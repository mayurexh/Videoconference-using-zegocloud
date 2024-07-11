from django.shortcuts import render,redirect
from .forms import UserRegisterationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def register_view(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html",{"success":"registeration successful"})
        else:
            err = form.errors.as_text()
            return render(request, "register.html", {"error": err})
    
    else:
        form = UserRegisterationForm()

    return render(request,"register.html",{"form":form})

@login_required
def dashboard_view(request): 
    return render(request, "dashboard.html", {"name":request.user.first_name})
        

@login_required
def videocall(request):
    return render(request, 'videocall.html', {"name": request.user.first_name+" "+ request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def joinroom(request):
    if request.method == "POST":
        roomID = request.POST["roomID"]
        return redirect("/meeting/?roomID="+roomID)
    return render(request, 'joinroom.html')



def home_view(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")
