from django.conf.urls import url
from django.contrib import admin
from .views import(
	Home_Page,
	login_view,
	register_view,
	logout_view,
	UserPosts,
	addpost,
	Follow
	)

urlpatterns = [
	url(r'^$', Home_Page),
	url(r'^login/', login_view,name='login'),
	url(r'^logout/', logout_view,name='logout'),
	url(r'^register/', register_view,name='register'),
	url(r'^Posts/(?P<userid>\d+)/$', UserPosts),
	url(r'^Posts/(?P<userid1>\d+)/(?P<userid2>\d+)/$', Follow),
	url(r'^Posts/(?P<userid>\d+)/addpost$', addpost),
	]