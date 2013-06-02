from quest.models import Question, Answer, Category
from django.contrib import admin

admin.site.register(Question, Answer, Category)
