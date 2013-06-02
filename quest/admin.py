from quest.models import Question, Answer, Catagory
from django.contrib import admin

admin.site.register(Question, Answer, Catagory)
