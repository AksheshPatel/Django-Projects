from django.conf.urls import url
from django.contrib import admin
from .views import(
	home_page,
	ask_user
	)

urlpatterns = [
	url(r'^$', home_page),
    url(r'^askuser/$', ask_user),
    # url(r'^Students/(?P<username>\w{1,50})/$', stu_info),
]