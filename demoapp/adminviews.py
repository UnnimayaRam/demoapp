from django.shortcuts import render, redirect

from demoapp.forms import courseaddform, notificationform, teacherloginform
from demoapp.models import studentadd, teacherlogin, courseadd, notification, complaint


def admin(request):
    return render(request,'admin/index.html')

def addcourse(request):
    form=courseaddform()
    u=request.user
    if request.method=='POST':
        form=courseaddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewcourse')
    return render(request,'admin/addcourse.html',{'form':form})


def updatecourse(request,id):
    course=courseadd.objects.get(id=id)
    form=courseaddform(instance=course)
    if request.method=='POST':
        form=courseaddform(request.POST or None,instance=course or None)
        if form.is_valid():
            c=form.save(commit=True)
            c.save()
            return redirect('viewcourse')
    return render(request,'admin/update_course.html',{'form':form})


def view_teacher(request):
    u = request.user
    data = teacherlogin.objects.all()

    return render(request, 'admin/view teacher.html', {'data': data})



def approveteacher(request,id):
    teacher=teacherlogin.objects.get(id=id)
    teacher.status=True
    teacher.status=1
    teacher.save()
    return redirect('view_teacher')


def delete_teacher(request, id):
    data = teacherlogin.objects.get(id=id)
    data.delete()
    return redirect('view_teacher')


def deletecourse(request,id):
    data = courseadd.objects.get(id=id)
    data.delete()
    return redirect('viewcourse')






def addnotification(request):
    form=notificationform()
    u=request.user
    if request.method=='POST':
        form=notificationform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('viewnotification')
    return render(request,'admin/addnotification.html',{'form':form})


def addteacher(request):
    form = teacherloginform()
    u = request.user
    if request.method == 'POST':
        form = teacherloginform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('admin')
    return render(request, 'admin/view teacher.html', {'form': form})

def viewnotification(request):
    u=request.user
    data=notification.objects.filter(user=u)
    return render(request,'admin/viewnotification.html',{'data':data})


def deletenotification(request,id):
    data=notification.objects.get(id=id)
    data.delete()
    return redirect('viewnotification')

def viewstudent1(request):
    s = request.user
    data = studentadd.objects.all()
    return render(request, 'admin/view_student.html', {'data': data})

def deletestudent(request,id):
    data=studentadd.objects.get(id=id)
    data.delete()
    return redirect('viewstudent1')

def viewcomplaint1(request):
    u = request.user
    data = complaint.objects.all()
    return render(request, 'admin/view_complaint.html', {'data': data})











