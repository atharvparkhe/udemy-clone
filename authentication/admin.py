from django.contrib import admin
from .models import *

class LearnerModelAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]

admin.site.register(LearnerModel, LearnerModelAdmin)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_verified"]

admin.site.register(TeacherModel, TeacherModelAdmin)