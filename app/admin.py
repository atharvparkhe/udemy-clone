from django.contrib import admin
from .models import *

admin.site.register(CategoryModel)
admin.site.register(SubCategoryModel)
admin.site.register(CourseModel)
admin.site.register(SectionModel)
admin.site.register(TopicModel)