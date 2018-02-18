from django.conf.urls import url
from django.contrib import admin
from .views import(
	home_page,
	)

urlpatterns = [
	url(r'^$', home_page),
    # url(r'^Teachers/$', all_teacher),
    # url(r'^Students/(?P<username>\w{1,50})/$', stu_info),
]