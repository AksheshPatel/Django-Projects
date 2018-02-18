# Create your views here.
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Word
from .forms import WordForm
from django.core.cache import cache

def home_page(request,username=None):
	# form = WordForm(request.POST or None)
	# if form.is_valid():
	#     word = form.cleaned_data.get("word_name")
	#     if word in cache:
	#     	return HttpResponse("<h1>"+cache.get(word)+"              From Cache </h1>")
	#     elif Word.objects.filter(word_name=word).count()>0:
	#     	meaning = Word.objects.
	#     	cache.set(word,meaning)
	#     	return HttpResponse("<h1>"+cache.get(word)+"              From Database </h1>")
	#     else :
	#     	form1 = WordMeaningForm(request.POST or None)
	#     	if form1.is_valid():
	#     		wordname = form.cleaned_data.get("word_name")
	#     		wordmeaning = form.cleaned_data.get("word_meaning")
	#     		cache.set(wordname,wordmeaning)
	#     		obj = Word(word_name=wordname,word_meaning=wordmeaning)
	#     		obj.save()
	#     		return redirect("/CacheApp")
	#     	return render(request, "form.html", {"form":form1, "title": "User Input"})
	#     return redirect("/CacheApp")
	# return render(request, "form.html", {"form":form, "title": "Find"})
	return HttpResponse("HELLO	")