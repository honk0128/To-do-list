from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Note, Task, Templates, Event, Room, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)

admin.site.register(Note)

# 11/18 추가
admin.site.register(Task)

admin.site.register(Templates)
admin.site.register(Event)

admin.site.register(Room)
admin.site.register(Message)
