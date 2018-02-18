# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Userpost,Userdetail,Userfollower
#from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterForm,AddPost,Userfollower

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

def Home_Page(request):
	return render(request,"LoginOrRegister.html",{})

def login_view(request):
	title = "Login"
	form = LoginForm(request.POST or None)
	if form.is_valid():

	    username = form.cleaned_data.get("username")
	    password = form.cleaned_data.get('password')
	    user = authenticate(username=username, password=password)
	    login(request, user)
	    user2 = Userdetail.objects.get(username=username)
	    #print user2.id
	    userid=str(user2.id)
	    return redirect("/Insta/Posts/"+userid)
	return render(request, "form.html", {"form":form, "title": title})

def register_view(request):
    print(request.user.is_authenticated())
    title = "Register"
    form = RegisterForm(request.POST or None, request.FILES or None)
    #form.save()
    print form.is_valid()
    
    if request.method == "POST":
    	form.photo = request.FILES['photo']
    	form.save()

    if form.is_valid():
    	print "HERERE"
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        new_Instauser = Userdetail(user=user,username=user.username)
        new_Instauser.save()
        login(request, new_user)
        user2 = Userdetail.objects.get(username=form.cleaned_data.get('username'))
        userid=str(user2.id)
        return redirect("/Insta/Posts/"+userid)

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/Insta/")

def UserPosts(request,userid=None):
	instance = get_object_or_404(Userdetail,id=int(userid))
	user = Userdetail.objects.get(id=int(userid))
	posts = user.post.all()
	follow = Userdetail.objects.all()

	context={
			"user":user,
			"userpost":posts,
			"username":user.username,
			"follow":follow
	}
	# #print User_Detail.objects.filter(user.id=int(userid))
	# #return HttpResponse("<h1>User Posts Here</h1>")
	return render(request,"Insta_Posts.html",context)

def addpost(request,userid=None):
	title = "Add Post"
	form = AddPost(request.POST or None, request.FILES or None)

	if form.is_valid():
		user = Userdetail.objects.get(id=int(userid))
		
		form.photo = request.FILES['photo']
		message = form.cleaned_data.get('message')
		newpost = Userpost(post=message,post_photo=form.photo)
		newpost.save()
		user.post.add(newpost)		
		return redirect ("/Insta/Posts/"+userid)

	context = {
        "form": form,
        "title": title
        }
        return render(request, "form.html",context)

def Follow(request,userid1=None,userid2=None):
	# user2 = Userdetail.objects.get(id=int(userid2))
	# user1 = Userdetail.objects.get(id=int(userid1))
	user2 = get_object_or_404(Userdetail,id=int(userid2))
	user1 = get_object_or_404(Userdetail,id=int(userid1))
	userfol = Userfollower(oriuser = user1)
	userfol.user = user2
	print user1.username,user2.username
	# userfol = Userfollower(user=user2)
	# userfol.save()
	# # user1.userfollower_set.add(userfol)
	# # user1.save()

	# print user1.userfollower_set.all()

	# fol = Userfollower.objects.all()

	# for f in fol:
	# 	print f.username

	return HttpResponse("<h1>Followers</h1>")