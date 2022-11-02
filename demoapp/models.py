from django.contrib.auth.models import AbstractUser


from django.db import models



# Create your models here.


GENDER_CHOICES={('F','FEMALE'),
                ('M','MALE'),
                ('O','OTHER')}

SUBJECT_CHOICES={
    ('MATHS','MATHS'),
    ('PHYSICS','PHYSICS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('BIOLOGY','BIOLOGY'),
    ('ENGLISH','ENGLISH'),
    ('LANGUAGE','LANGUAGE')
}

ANSWER_CHOICES={
    ('option1','option1'),
    ('option2','option2'),
    ('option3','option3'),
    ('option4','option4')
}



class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)



class teacherlogin(models.Model):
    user=models.OneToOneField(Login, on_delete=models.CASCADE,related_name='teacher')
    tid=models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=30,choices=GENDER_CHOICES)
    address = models.TextField(max_length=200, null=True, blank=True)
    subject= models.CharField(max_length=50,choices=SUBJECT_CHOICES)
    phone_no=models.IntegerField(null=True)
    image=models.ImageField()
    status = models.IntegerField(default=0)

class courseadd(models.Model):
    user=models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    dept=models.CharField(max_length=30)
    subject=models.CharField(max_length=40)
    teacher=models.CharField(max_length=50)
    description=models.TextField(max_length=200, null=True, blank=True)



class studentadd(models.Model) :
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    dob=models.DateField()
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(max_length=200)
    year=models.CharField(max_length=30)
    dept=models.CharField(max_length=100)
    phone=models.IntegerField(null=True,blank=True)
    sid=models.CharField(max_length=30)
    gender=models.CharField(max_length=100)
    photo=models.ImageField()


class notification(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200,null=True,blank=True)

class complaint(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    s_name=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    description=models.TextField(max_length=200)
    reply=models.TextField(max_length=200,null=True,blank=True)


class notes(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    note = models.FileField()

class assignment(models.Model):
    user=models.ForeignKey(Login, on_delete=models.CASCADE)
    t_name=models.CharField(max_length=100)
    subject= models.CharField(max_length=50,choices=SUBJECT_CHOICES)
    chap=models.IntegerField(null=True, blank=True)
    topic=models.CharField(max_length=100)


class uploadassign(models.Model):
    user=models.ForeignKey(Login, on_delete=models.CASCADE)
    Studentname=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    Assignment=models.FileField()
class Attendence(models.Model):
    student=models.ForeignKey(studentadd,on_delete=models.CASCADE,related_name='attendence')
    date=models.DateField()
    attendence=models.CharField(max_length=10)
    time=models.TimeField()


class leave(models.Model):
    student=models.ForeignKey(studentadd,on_delete=models.CASCADE,null=True,blank=True)
    s_name=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    date=models.DateField()
    status = models.IntegerField(default=0)



class exam(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    question=models.TextField(max_length=200)
    ans=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    checkans=models.BooleanField(default=False)



    def __str__(self):
        return self.s_name
