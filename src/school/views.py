# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student2,Course2,Teacher2
#from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
# Create your views here.

# def all_student(request):
# 	allstudent = Student.objects.all()
# 	html=''
# 	for stu in allstudent.iterator():
# 		html+='<a href="'+stu.student_name+'">'+stu.student_name+'</a><br>'
# 	return HttpResponse(html)

def all_student2(request):
	allstudent = Student2.objects.all()
	html=''
	for stu in allstudent.iterator():
		html+='<a href="'+stu.student_name+'">'+stu.student_name+'</a><br>'
	return HttpResponse(html)

# def all_course(request):
# 	allcourse = Course.objects.all()
# 	html=''
# 	for stu in allcourse.iterator():
# 		html+='<a href="'+stu.course_name+'">'+stu.course_name+'</a><br>'
# 	return HttpResponse(html)

def all_course2(request):
	allcourse = Course2.objects.all()
	html=''
	l=[]
	for stu in allcourse.iterator():
		if stu.course_name in l:
			continue
		else:
			html+='<a href="'+stu.course_name+'">'+stu.course_name+'</a><br>'
			l.append(stu.course_name)
	return HttpResponse(html)

# def all_teacher(request):
# 	allteacher = Teacher.objects.all()
# 	html=''
# 	for stu in allteacher.iterator():
# 		html+='<a href="'+stu.teacher_name+'">'+stu.teacher_name+'</a><br>'
# 	return HttpResponse(html)

def all_teacher2(request):
	allteacher = Teacher2.objects.all()
	html=''
	for stu in allteacher.iterator():
		html+='<a href="'+stu.teacher_name+'">'+stu.teacher_name+'</a><br>'
	return HttpResponse(html)	

def test(request):
	return render(request,"test.html",{})

# def stu_info(request,username=None):
# 	user = Student.objects.get(student_name=username)
# 	print user
# 	#print getattr(user, 'id')
# 	#print user.values(student_name=user.student_name)
# 	context={
# 			#"cc":Student.objects.get(student_name=user.student_name)
# 			"cc":user		
# 	}
# 	return render(request,"allstudent.html",context)

def stu_info2(request,username=None):
	user = Student2.objects.get(student_name=username) 

	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc":user.course2_set.all(),
			"name":user.student_name
	}
	return render(request,"allstudent.html",context)

# def tea_info(request,teachername=None):
# 	user = Teacher.objects.get(teacher_name=teachername)
# 	#print getattr(user, 'id')
# 	#print user.values(student_name=user.student_name)
# 	context={
# 			#"cc":Student.objects.get(student_name=user.student_name)
# 			"cc":user		
# 	}
# 	return render(request,"allteacher.html",context)

#@login_required
def tea_info2(request,teachername=None):
	teach = Teacher2.objects.get(teacher_name=teachername)
	print 
	
	#print getattr(user, 'id')
	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc" : teach.course2_set.all(),
			"name": teach.teacher_name		
	}
	return render(request,"allteacher.html",context)

def login_view(request):

   # print(request.user.is_authenticated())
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():

	    username = form.cleaned_data.get("username")
	    password = form.cleaned_data.get('password')
	    user = authenticate(username=username, password=password)
	    login(request, user)
	    return redirect("/")
	return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
	
