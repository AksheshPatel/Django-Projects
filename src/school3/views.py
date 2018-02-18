from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student22,Course22,Teacher22,Teacher3,Student3
#from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

def all_student22(request):
	allstudent = Student22.objects.all()
	html=''
	for stu in allstudent.iterator():
		html+='<a href="'+stu.student_name+'">'+stu.student_name+'</a><br>'
	return HttpResponse(html)

def all_student3(request):
	allstudent = Student3.objects.all()
	html=''
	for stu in allstudent.iterator():
		html+='<a href="'+stu.student_name+'">'+stu.student_name+'</a><br>'
	return HttpResponse(html)

def all_course22(request):
	allcourse = Course22.objects.all()
	html=''
	l=[]
	for stu in allcourse.iterator():
		if stu.course_name in l:
			continue
		else:
			html+='<a href="'+stu.course_name+'">'+stu.course_name+'</a><br>'
			l.append(stu.course_name)
	return HttpResponse(html)

def all_teacher22(request):
	allteacher = Teacher22.objects.all()
	if request.user.is_authenticated():
		print "Logged INNN"
	else:
		return render(request,"LoginOrRegister.html",{})
	html=''
	for stu in allteacher.iterator():
		html+='<a href="'+stu.teacher_name+'">'+stu.teacher_name+'</a><br>'
	return HttpResponse(html)

def all_teacher3(request):
	allteacher = Teacher3.objects.all()
	l=[]
	if request.user.is_authenticated():
		print "Logged INNN"
	else:
		return render(request,"LoginOrRegister.html",{})
	html=''
	
	for stu in allteacher.iterator():
		l.append(stu.teacher_name)
		html+='<a href="'+stu.teacher_name+'">'+stu.teacher_name+'</a><br>'

	return HttpResponse(html)	


def test(request):
	return render(request,"test.html",{})

def stu_info22(request,username=None):
	user = Student22.objects.get(student_name=username) 
	print 
	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc":user.course_name,
			"name":user.student_name
	}
	return render(request,"allstudent22.html",context)

def cou_info22(request,coursename=None):
	print coursename
	cou = Course22.objects.get(course_name=coursename)

	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"students":cou.student3_set.all(),
			"teachers":cou.teacher3_set.all(),
			"course":cou.course_name
	}
	return render(request,"allcourse.html",context)

def stu_info3(request,username=None):
	user = Student3.objects.get(student_name=username) 
	print user.course_name.all()
	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc":user.course_name.all(),
			"name":user.student_name
	}
	return render(request,"allstudent22.html",context)

#@login_required
def tea_info22(request,teachername=None):
	teach = Teacher22.objects.get(teacher_name=teachername)
	print teach
	#print getattr(user, 'id')
	#print user.values(student_name=user.student_name)
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc" : teach.course22_set.all(),
			"name": teach.teacher_name,
			"user":request.user		
	}
	return render(request,"allteacher22.html",context)

def tea_info3(request,teachername=None):
	teach = Teacher3.objects.get(teacher_name=teachername)
	#print teach.course_name.all()
	#stu = Student3.objects.all()
	#teach1=Teacher3.objects.filter(teacher_name=teachername)[:1].get()
	cou = teach.course_name.all()[:1].get()
	stu =  cou.student3_set.all()
	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"cc" : teach.course_name.all(),
			"name" : teach,
			"students":stu		
	}
	return render(request,"allteacher22.html",context)

def addteacher_info(request,teachername=None):
	tea = Teacher3.objects.get(teacher_name=teachername)
	stu = Student3.objects.all()
	
	if request.method == "POST":
		stu_name=Student3.objects.get(student_name = request.POST['stu_name'])
		cou_name=Course22.objects.get(course_name =  request.POST['cou_name'])
		stu_name.course_name.add(cou_name)
		stu_name.save()
		# student = Student3(id=None,student_name=stu_name,course_name=Course22.objects.get(course_name=cou_name))
		# student.save()
		return redirect("/School3/Teachers3/"+teachername)

	context={
			#"cc":Student.objects.get(student_name=user.student_name)
			"teacher" : tea.teacher_name,
			"student" : stu,
			"course": tea.course_name.all()	
	}
	return render(request,"addstudent.html",context)

def login_view(request):

   # print(request.user.is_authenticated())
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():

	    username = form.cleaned_data.get("username")
	    password = form.cleaned_data.get('password')
	    user = authenticate(username=username, password=password)
	    login(request, user)
	    return redirect("/School3/")
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
        teacher = Teacher3(teacher_name=user.username)
        teacher.save()
        login(request, new_user)
        return redirect("/School3/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/School3/")