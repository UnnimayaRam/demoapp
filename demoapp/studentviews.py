from django.shortcuts import render, redirect

from demoapp.forms import LoginForm, studentloginform, complaintform, assignmentform, uploadassignmentform, leaveform
from demoapp.models import studentadd, teacherlogin, notification, notes, assignment, exam


def student(request):
    return render(request,'student/index.html')

def studentregister(request):
    form= LoginForm()
    form1 = studentloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = studentloginform(request.POST, request.FILES)
        print(form1)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_student= True
            user.save()
            s=form1.save()
            s.user=user
            s.save()

            return redirect('viewstudent')
    return render(request,'teacher/addstudent.html',{'form':form,'form1':form1})


def studentprofile(request):
    user=request.user
    data=studentadd.objects.all()
    return render(request,'student/viewprofile.html',{'data':data})

def addcomplaint(request):
    form = complaintform()
    u = request.user
    if request.method == 'POST':
        form = complaintform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('student')
    return render(request,'student/add_complaint.html',{'form':form})

def addleave(request):
    form =leaveform()
    u=request.user
    if request.method=='POST':
        form=leaveform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('student')
    return render(request,'student/add_leave.html',{'form':form})



def view_teacher1(request):
    u = request.user
    data = teacherlogin.objects.all()

    return render(request, 'student/teacherview.html', {'data': data})

def viewnotification2(request):
    u=request.user
    data=notification.objects.filter(user=u)
    return render(request,'student/view_notification.html',{'data':data})

def view_notes(request):
    u = request.user
    data = notes.objects.filter(user=u)
    return render(request, 'student/viewnotes.html', {'data': data})

def viewassignment(request):
    u=request.user
    data=assignment.objects.filter(user=u)
    return render(request,'student/view_assignment.html',{'data':data})
def viewexam(request,id):
    u=request.user
    data=exam.objects.filter(id=id)
    return render(request,'student/view_exam.html',{'data':data})

def uploadassignment(request):
    form=uploadassignmentform()
    u=request.user
    if request.method=='POST':
        form=uploadassignmentform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('viewassignment')
    return render(request,'student/upload_assignment.html',{'form':form})


def take_test(request,id):
    d=exam.objects.get(id=id)
    emark=None
    question=exam.objects.filter()












