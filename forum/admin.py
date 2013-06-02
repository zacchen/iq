from django.contrib import admin
from forum.models import Post, Reply, Catagory

admin.site.register(Post, Reply, Catagory)

