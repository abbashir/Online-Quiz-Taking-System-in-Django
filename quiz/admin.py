from django.contrib import admin
from .models import Subject, Question,QuestionChoice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(QuestionChoice)
