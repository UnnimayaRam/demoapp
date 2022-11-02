from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from demoapp.forms import complaintform, teacherloginform, noteform, assignmentform, examform
from demoapp.models import complaint, teacherlogin, studentadd, notification, notes, uploadassign, Attendence, leave, \
    exam


def teacher(request):
    return render(request,'teacher/index.html')

def viewtprofile(request):
    u = request.user
    data = teacherlogin.objects.all()
    return render(request,'teacher/profileview.html',{'data':data})



def update_teacher(request,id):
    profile=teacherlogin.objects.get(id=id)
    form2=teacherloginform(instance=profile)
    if request.method =='POST':
        form2=teacherloginform(request.POST or None,instance=profile or None)
        if form2.is_valid:
            teacher = form2.save(commit=True)
            teacher.is_teacher=True
            teacher.save()
            return redirect('viewtprofile')
    return render(request,'teacher/profileupdate.html',{'form2':form2})





def viewcomplaint(request):
    u = request.user
    data = complaint.objects.all()
    return render(request, 'teacher/view_complaint.html', {'data': data})

def viewleave(request):
    u=request.user
    data=leave.objects.all()
    return render(request,'teacher/viewandapproveleave.html',{'data':data})

def approveleave(request,id):
    Leave=leave.objects.get(id=id)
    Leave.status=True
    Leave.status=1
    Leave.save()
    return redirect('viewleave')

def deleteleave(request,id):
    data=leave.objects.get(id=id)
    data.delete()
    return redirect('viewleave')


def add_reply(request,id):
    cmplt=complaint.objects.get(id=id)
    form=complaintform(instance=cmplt)
    if request.method=='POST':
        r=request.POST.get('reply')
        complaint.reply=r
        complaint.save()
        messages.info(request,'Reply send for complaints')
        return redirect('viewcomplaint')
    return render(request,'teacher/reply.html',{'cmplt':cmplt,'form':form})





def addreply(request):
    form = complaintform()
    u = request.user

    if request.method == 'POST':
        form = complaintform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('viewcomplaint')
    return render(request, 'teacher/reply.html', {'form': form,'data':data})


def viewstudent(request):
    s = request.user
    data = studentadd.objects.all()
    return render(request, 'teacher/view student.html', {'data': data})

def delete_student(request,id):
    data=studentadd.objects.get(id=id)
    data.delete()
    return redirect('viewstudent')

def viewnotification1(request):
    u=request.user
    data=notification.objects.filter(user=u)
    return render(request,'teacher/view_notification.html',{'data':data})


def addnotes(request):
    form=noteform()
    u=request.user
    if request.method=='POST':
        form=noteform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('view_notes')
    return render(request, 'teacher/add_notes.html', {'form': form})




def addassignment(request):
    form=assignmentform()
    u=request.user
    if request.method=='POST':
        form=assignmentform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('teacher')
    return render(request,'teacher/add_assignment.html',{'form':form})


def tviewassignment(request):
    u=request.user
    data=uploadassign.objects.filter(user=u)
    return render(request,'teacher/view_assignment.html',{'data':data})

def addattendence(request):
    data=studentadd.objects.all()
    return render(request,'teacher/add_attendence.html',{'data':data})

# now = datetime.datetime.now()

def mark_attendence(request,id):
    name=studentadd.objects.get(id=id)
    att=Attendence.objects.filter(student=name,date=datetime.date.today())
    if att.exists():
        messages.info(request,"Todays attendence already marked for this student")
        return redirect('addattendence')
    else:
        if request.method=='POST':
            atndnc=request.POST.get('attendence')
            Attendence(student=name,date=datetime.date.today(),attendence=atndnc,time=now.time()).save()
            messages.info(request,"attendence added successfully")
            return redirect('addattendence')
    return render(request,'teacher/markattendence.html')

def viewattendence(request):
    value_list=Attendence.objects.values_list('date',flat=True).distinct()
    attend={}
    for value in value_list:
        attend[value]=Attendence.object




def addexam(request):
    form=examform()
    u=request.user
    if request.method=='POST':
        form=examform(request.POST or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            messages.info(request,'successfully')
            return redirect('viewexams')
    return render(request,'teacher/add_exam.html',{'form':form})

def viewexams(request):
    u=request.user
    data=exam.objects.filter(user=u)
    return render(request,'teacher/view_exams.html',{'data':data})










