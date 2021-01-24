from django.contrib import admin
from .models import Profile, Post, Like, Friend, Comment, Favourites

# Register your models here.
admin.site.register(Profile)

admin.site.register(Post)

admin.site.register(Like)

admin.site.register(Friend)

admin.site.register(Comment)

admin.site.register(Favourites)