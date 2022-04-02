from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("home")
            else:
                messages.error(request, "Please Check Email and Password!!!")
                return redirect("Login")
        return render(request, "login.html")
    else:
        return redirect("home")


def register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            name = request.POST['name']
            mobile_no = request.POST['mobile_no']
            dob = request.POST['dob']
            if password==cpassword:
                user = User.objects.filter(email=email)
                if user:
                    messages.error(request, "User Already Exits!!!")
                    return redirect("register")
                else:
                    User.objects.create_user(email=email, password=password,name=name,mobile_no=mobile_no,date_of_birth=dob)
                    return redirect("Login")
            else:
                messages.error(request, "Password didn't match!!!")
                return redirect("register")
        return render(request, "register.html")
    else:
        return redirect("home")

#admin work
@login_required(login_url='login')
def index(request):
    ap = Apps.objects.all()
    return render(request, "Head/home-page.html",{'ap':ap})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect("Login")

#add app
@login_required(login_url='login')
def add_app(request):
    if request.method=='POST':
        img = request.FILES['image']
        name = request.POST['name']
        link = request.POST['link']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        point = request.POST['point']

        Apps.objects.create(img=img,app_link=link,app_name=name,category=category,sub_category=sub_category,point=point)
        return redirect("index")
    return render(request, "Head/add-apps.html")




#user work
@login_required(login_url='login')
def home(request):
    app = Apps.objects.all()
    p = Points.objects.all()
    for po in p:
        app = app.exclude(id=po.x.id)
    return render(request, "user/home-page.html",{'app':app})

@login_required(login_url='login')
def app(request,id):
    ap = Apps.objects.get(id=id)
    return render(request, "user/app-details.html",{'app':ap})

@login_required(login_url='login')
def view_app(request,id):
    app = Apps.objects.get(id=id)
    return render(request, "Head/app-details.html",{'app':app})


@login_required(login_url='login')
def add_point(request):    
    if request.method=='POST':
            user = request.user
            ap = request.POST['app']
            img = request.FILES['image']
            ap = Apps.objects.get(id=ap)
            Points.objects.create(user=user,x=ap,success_img=img,status="complate")
            return redirect("task")

@login_required(login_url='login')
def point(request):
    app = Points.objects.filter(Q(user=request.user) & Q(status="complate"))

    app_complete = 0
    for i in app:
        app_complete+=i.x.point

    return render(request, "user/point.html",{'app_complete':app_complete})


@login_required(login_url='login')
def task(request):
    app = Points.objects.filter(Q(user=request.user) & Q(status="complate"))
    return render(request, "user/task.html",{'app':app})


@login_required(login_url='login')
def edit_profile(request):
    if request.method=='POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        user = User.objects.filter(email=request.user).update(name=name,mobile_no=mobile,date_of_birth=dob)
        return redirect("edit_profile")
    return render(request, "user/edit-profile.html")