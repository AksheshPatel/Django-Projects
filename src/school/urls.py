from django.conf.urls import url
from django.contrib import admin
from .views import(
	# all_student,
	# all_course,
	# all_teacher,
	# test,
	# stu_info,
	# tea_info,
	test,
	all_student2,
	all_course2,
	all_teacher2,
	stu_info2,
	tea_info2,
	login_view,
	register_view,
	logout_view
	)

urlpatterns = [
	url(r'^$', test),
    # url(r'^Students/$', all_student),
    # url(r'^Courses/$', all_course),
    # url(r'^Teachers/$', all_teacher),
    # url(r'^Students/(?P<username>\w{1,50})/$', stu_info),
    # url(r'^Teachers/(?P<teachername>\w{1,50})/$', tea_info),
    url(r'^Students2/$', all_student2),
    url(r'^Courses2/$', all_course2),
    url(r'^Teachers2/$', all_teacher2),
    url(r'^Students2/(?P<username>\w{1,50})/$', stu_info2),
    url(r'^Teachers2/(?P<teachername>\w{1,50})/$', tea_info2),
    url(r'^login/', login_view,name='login'),
    url(r'^register/', register_view,name='register'),
    url(r'^logout/', logout_view,name='logout'),
]