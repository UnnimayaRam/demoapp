from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, teacherlogin, courseadd, studentadd, notification, complaint, notes, assignment, \
    uploadassign, Attendence, leave, exam


class DateInput(forms.DateInput):
    input_type = "date"

class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label="password")
    password2=forms.CharField(widget=forms.PasswordInput,label="confirm password")

    class Meta:
        model=Login
        fields=("username","password1","password2")


GENDER_CHOICES={('F','FEMALE'),
                ('M','MALE'),
                ('O','OTHER')}

class teacherloginform(forms.ModelForm):

    class Meta:
        model=teacherlogin
        fields=("name","age","gender","address","subject","phone_no","image")


class courseaddform(forms.ModelForm):

    class Meta:
        model=courseadd
        fields=("dept","subject","teacher","description")


class studentloginform(forms.ModelForm):
    dob=forms.DateField(widget=DateInput)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)

    class Meta:

        model=studentadd
        fields=("name","dob","age","address","year","dept","phone","sid","gender","photo")




class notificationform(forms.ModelForm):
    class Meta:
        model=notification
        fields=("name","description")


class complaintform(forms.ModelForm):
    # date=forms.DateField(widget=DateInput)
    class Meta:
        model=complaint
        fields=("s_name","description")


class noteform(forms.ModelForm):
    class Meta:
        model=notes
        fields=("title","subject","note")

class assignmentform(forms.ModelForm):
    class Meta:
        model=assignment
        fields=("t_name","subject","chap","topic")


class uploadassignmentform(forms.ModelForm):
    class Meta:
        model=uploadassign
        fields=("Studentname","Assignment")

class attendenceform(forms.ModelForm):
    class Meta:
        model=Attendence
        fields=('student','attendence')


class leaveform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=leave
        fields=('s_name','description','date')




ANSWER_CHOICES={
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4')
}

class examform(forms.ModelForm):
    ans= forms.ChoiceField(widget=forms.RadioSelect, choices=ANSWER_CHOICES)
    class Meta:
        model=exam
        fields=('question','ans','option1','option2','option3','option4','checkans')




