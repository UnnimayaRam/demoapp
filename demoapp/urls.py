


from django.urls import path

from demoapp import views, adminviews, studentviews, teacherviews

urlpatterns = [
    path('',views.home,name='home'),
    path('loginview',views.loginview,name='loginview'),


    ###admin
    path('admin',adminviews.admin,name='admin'),
    path('approveteacher/<int:id>/',adminviews.approveteacher,name='approveteacher'),
    path('view_teacher',adminviews.view_teacher,name='view_teacher'),
    path('viewstudent1',adminviews.viewstudent1,name='viewstudent1'),
    path('addnotification',adminviews.addnotification,name='addnotification'),
    path('updatenotification/<int:id>/',views.updatenotification,name='updatenotification'),
    path('addcourse',adminviews.addcourse,name='addcourse'),
    path('updatecourse/<int:id>/',adminviews.updatecourse,name='updatecourse'),
    path('delete_teacher/<int:id>/',adminviews.delete_teacher,name='delete_teacher'),
    path('deletecourse/<int:id>/',adminviews.deletecourse,name='deletecourse'),
    path('deletestudent/<int:id>/',adminviews.deletestudent,name='deletestudent'),
    path('deletenotification/<int:id>/',adminviews.deletenotification,name='deletenotification'),
    path('viewnotification',adminviews.viewnotification,name='viewnotification'),
    path('viewcomplaint1',adminviews.viewcomplaint1,name='viewcomplaint1'),

    ###student
    path('student',studentviews.student,name='student'),
    path('studentregister',studentviews.studentregister,name='studentregister'),
    path('studentprofile',studentviews.studentprofile,name='studentprofile'),
    path('addcomplaint',studentviews.addcomplaint,name='addcomplaint'),
    path('view_teacher1',studentviews.view_teacher1,name='view_teacher1'),
    path('viewnotification2',studentviews.viewnotification2,name='viewnotification2'),
    path('view_notes',studentviews.view_notes,name='view_notes'),
    path('viewexam',studentviews.viewexam,name='viewexam'),
    path('viewassignment',studentviews.viewassignment,name='viewassignment'),
    path('uploadassignment',studentviews.uploadassignment,name='uploadassignment'),
    path('addleave',studentviews.addleave,name='addleave'),


    ###teacher
    path('viewstudent',teacherviews.viewstudent,name='viewstudent'),
    path('delete_student/<int:id>/',teacherviews.delete_student,name='delete_student'),
    path('viewcomplaint',teacherviews.viewcomplaint,name='viewcomplaint'),
    path('add_reply/<int:id>/',teacherviews.add_reply,name='add_reply'),
    path('teacher',teacherviews.teacher,name='teacher'),
    path('viewtprofile',teacherviews.viewtprofile,name='viewtprofile'),
    path('viewnotification1',teacherviews.viewnotification1,name='viewnotification1'),
    path('register',views.register,name='register'),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('addnotes',teacherviews.addnotes,name='addnotes'),
    path('addassignment',teacherviews.addassignment,name='addassignment'),
    path('tviewassignment',teacherviews.tviewassignment,name='tviewassignment'),
    path('viewleave',teacherviews.viewleave,name='viewleave'),
    path('approveleave/<int:id>/',teacherviews.approveleave,name='approveleave'),
    path('deleteleave/<int:id>/',teacherviews.deleteleave,name='deleteleave'),
    path('addattendence',teacherviews.addattendence,name='addattendence'),
    path('mark_attendence/<int:id>/',teacherviews.mark_attendence,name='mark_attendence'),
    path('addexam',teacherviews.addexam,name='addexam'),
    path('update_teacher/<int:id>/',teacherviews.update_teacher,name='update_teacher'),
    path('viewexams',teacherviews.viewexams,name='viewexams'),


]