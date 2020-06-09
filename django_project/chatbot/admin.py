from django.contrib import admin

from chatbot.models import User, Question, QuestionText, Response


admin.site.register(User)
admin.site.register(Question)
admin.site.register(QuestionText)
admin.site.register(Response)
