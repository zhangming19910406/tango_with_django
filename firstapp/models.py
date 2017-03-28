from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250, default="https://qph.ec.quoracdn.net/main-qimg-016319d146ee93a464cb11870001b29c")
    cover = models.FileField(upload_to='cover_image', null=True)
    # content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(auto_now_add=True, null=True)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/", toolbars='besttome', filePath='uploads/files/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=10)
    avatar = models.CharField(max_length=100, default="http://semantic-ui.com/images/avatar/small/matt.jpg")
    content = models.TextField()
    createtime = models.DateField(auto_now=True)
    belong_to = models.ForeignKey(to=Article, related_name='under_comment')

    def __str__(self):
        return self.content


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')


class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, related_name='voted_tickets', null=True)
    video = models.ForeignKey(to=Article, related_name='tickets', null=True)
    VOTE_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)