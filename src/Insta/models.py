from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
 
class Userpost(models.Model):
    post = models.TextField()
    post_photo = models.ImageField(upload_to='Images',null=True,blank=True)
    # post_User = models.ManyToManyField(User_Detail)

class Userdetail(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=50,default='')
    photo = models.ImageField(upload_to='Images',null=True,blank=True)
    post = models.ManyToManyField(Userpost)

    def __unicode__(self):
        return  self.username

# class Userlike(models.Model):
# 	post = models.ForeignKey(Userpost, related_name='liked_post')
# 	user = models.ForeignKey(Userdetail, related_name='liker')

# 	def __unicode__(self):
# 		return '{} : {}'.format(self.user, self.post)

class Userfollower(models.Model):
	oriuser = models.OneToOneField(User,null=True)
	user = models.ForeignKey(Userdetail)

	def __unicode__(self):
		return '{}'.format(self.oriuser)

# class Usercomment(models.Model):
#     post = models.ForeignKey(Userpost, related_name='post_comments')
#     user = models.ForeignKey(Userdetail, related_name='commenter')
#     date_created = models.DateTimeField(auto_now_add=True)
#     content = models.CharField(max_length=120)

#     def __unicode__(self):
#         return self.content

#     def __str__(self):
#         return self.content