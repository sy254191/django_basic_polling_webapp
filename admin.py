from django.contrib import admin
from .models import Choice,Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
]
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
# Register your models here.
