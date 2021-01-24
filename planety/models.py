from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from PIL import Image
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='author')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    image = models.ImageField(blank=True, null=True, upload_to='post_pics')
    caption  = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    video = models.FileField(upload_to='video_posts', null=True, blank=True)

    def __str__(self):
        return self.caption

    @property
    def num_favourites(self):
        return self.favourite.all().count()

    @property
    def num_likes(self):
        return self.liked.all().count()

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk':self.pk})
#############################################
LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike')

)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

############################################

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address  = models.CharField(max_length=500)
    Dob = models.DateField(blank=True, null=True)
    cover_photos = models.ImageField(default='cover3.jpeg',upload_to='cover_pics')
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user.username} Profile'

###########################################

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who sent the request
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')  # who will receive the request
    # sender = models.CharField(max_length=20, default='requested')
    status = models.CharField(max_length=20, default='requested')
    created_at = models.DateTimeField(default=now)

###########################################

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_updated = models.DateTimeField(auto_now=True)
    
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})

#############################################

FAV_CHOICES = (
    ('Save','Save'),
    ('Saved','Saved')
)

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=FAV_CHOICES,default='Save',max_length=10)

    def __str__(self):
        return str(self.post)