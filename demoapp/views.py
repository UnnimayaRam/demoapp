
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from demoapp.adminviews import admin
from demoapp.forms import LoginForm, teacherloginform, courseaddform, studentloginform, notificationform, complaintform
from demoapp.models import teacherlogin, courseadd, studentadd, notification, complaint
from demoapp.studentviews import student
from demoapp.teacherviews import teacher


def home(request):
    return render(request,'index.html')

def loginview(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect(admin)
        if user is not None and user.is_student:
            login(request, user)
            return redirect(student)
        if user is not None and user.is_teacher:
            if user.teacher.status== True:
                login(request, user)
                return redirect(teacher)
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'admin/login.html')


def register(request):
    form1=LoginForm()
    form2=teacherloginform()
    if request.method=='POST':
        form1=LoginForm(request.POST)
        form2=teacherloginform(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.is_teacher=True
            user.save()
            teacher=form2.save(commit=False)
            teacher.user=user
            teacher.save()
            return redirect('home')

    return render(request,'registration.html',{'form1':form1,'form2':form2})


def viewcourse(request):
    u=request.user
    data=courseadd.objects.filter(user=u)
    return render(request,'admin/viewcourse.html',{'data':data})



###notification




def updatenotification(request,id):
    view_notification=notification.objects.get(id=id)
    form=notificationform(instance=view_notification)
    if request.method=='POST':
        form=notificationform(request.POST or None,request.FILES or None)
        if form.is_valid:
            notifi=form.save(commit=False)
            notifi.save()
            return redirect('viewnotification')
    return render(request,'admin/notificationupdate.html',{'form':form})


