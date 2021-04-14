# RESOURCE SERVER ADMIN FILE
# ---------------------------------------------------------------------------------

from django.contrib import admin
from .models import Post, Comment,  Profile , Topic


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Profile)