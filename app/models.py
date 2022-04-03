from django.db import models
from authentication.models import TeacherModel
from base.models import BaseModel
from .validators import *


class CategoryModel(BaseModel):
    category_name = models.CharField(max_length=50)
    category_img = models.ImageField(upload_to="categories", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.category_name


class SubCategoryModel(BaseModel):
    category = models.ForeignKey(CategoryModel, related_name="sub_categories", on_delete=models.CASCADE)
    sub_cat_name = models.CharField(max_length=50)
    def __str__(self):
        return self.sub_cat_name


class CourseModel(BaseModel):
    teacher = models.ForeignKey(TeacherModel, related_name="course_teacher", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    content = models.TextField()
    price = models.FloatField(default=100)
    sub_category = models.ForeignKey(SubCategoryModel, related_name="course_sub_category", on_delete=models.PROTECT)
    img = models.ImageField(upload_to='courses')
    likes = models.PositiveIntegerField(default=0)
    ratings = models.FloatField(default=0, validators=[validate_stars])
    def __str__(self):
        return self.title


class SectionModel(BaseModel):
    course = models.ForeignKey(CourseModel, related_name="course_sections", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    def __str__(self):
        return self.title


class TopicModel(BaseModel):
    section = models.ForeignKey(SectionModel, related_name="section_topic", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    file = models.FileField(upload_to="topic_file", max_length=100, null=True, blank=True)
    video = models.URLField(max_length=250)
    def __str__(self):
        return self.title

