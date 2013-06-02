from django.contrib import admin
from blog.forum import Post, Reply, Catagory

admin.site.register(Post, Reply, Catagory)

