from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import WordName,WordMeaning
from .forms import WordForm,WordMeaningForm
from django.core.cache import cache

def home_page(request,username=None):
	form = WordForm(request.POST or None)
	if form.is_valid():

	    word = form.cleaned_data.get("word_name")
	    if word in cache:
	    	return HttpResponse("<h1>"+cache.get(word)+"              From Cache </h1>")
	    elif WordMeaning.objects.filter(w_name=word).count()>0:
	    	meaning = WordMeaning.objects.get(w_name=word)
	    	cache.set(word,meaning.w_meaning)
	    	return HttpResponse("<h1>"+cache.get(word)+"              From Database </h1>")
	    else :
	    	# form1 = WordMeaningForm(request.POST or None)
	    	# #form1.save()
	    	# if form1.is_valid():
	    	# 	print "VALID"
	    	# 	wordname = form1.cleaned_data.get("w_name")
	    	# 	wordmeaning = form1.cleaned_data.get("w_meaning")
	    	# 	print wordname
	    	# 	cache.set(wordname,wordmeaning)
	    	# 	obj = WordMeaning(w_name=wordname,w_meaning=wordmeaning)
	    	# 	obj.save()
	    	# 	return redirect("/CacheApp")
	    	# else:
	    	# 	print "Not Valid"
	    	# return render(request, "form.html", {"form":form1, "title": "User Input"})

	    	return redirect("/Cache/askuser")
	    return redirect("/Cache")
	return render(request, "form.html", {"form":form, "title": "Find"})
	return HttpResponse("HELLO	")	
	#return HttpResponse("HELLO	")

def ask_user(request):
	form1 = WordMeaningForm(request.POST or None)
	if form1.is_valid():
	    print "VALID"
	    wordname = form1.cleaned_data.get("w_name")
	    wordmeaning = form1.cleaned_data.get("w_meaning")
	    print wordname
	    cache.set(wordname,wordmeaning)
	    obj = WordMeaning(w_name=wordname,w_meaning=wordmeaning)
	    obj.save()
	    return redirect("/CacheApp")
	else:
	    print "Not Valid"
	    return render(request, "form.html", {"form":form1, "title": "User Input"})
	return redirect("/Cache")
