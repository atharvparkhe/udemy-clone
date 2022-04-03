from rest_framework import serializers
from authentication.serializers import TeacherNameSerializer
from .models import *


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ["sub_cat_name", "id"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name", "category_img"]

class TopicNameSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = ["title"]

class TopicSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        exclude = ["created_at", "updated_at", "section"]

class SectionNameSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ["title"]

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ["title", "desc"]

class SectionWithTopicsSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField()
    class Meta:
        model = SectionModel
        fields = ["title", "desc"]
    def get_topics(self, obj):
        try:
            res = []
            objs = obj.section_topic.all()
            serializer = TopicSerilaizer(objs ,many=True)
            res = serializer.data
            return res
        except Exception as e:
            print(e)

class MultiCourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ["id", "title", "desc", "img"]

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer()
    sub_category = SubcategorySerializer()
    sections = serializers.SerializerMethodField()
    class Meta:
        model = CourseModel
        exclude = ["created_at", "updated_at"]
    def get_sections(self, obj):
        try:
            sec = []
            objs = obj.course_sections.all()
            serializer = SectionSerializer(objs ,many=True)
            sec = serializer.data
            return sec
        except Exception as e:
            print(e)

class TopicSerilaizer(serializers.ModelSerializer):
    section = SectionNameSerilizer()
    class Meta:
        model = TopicModel
        exclude = ["created_at", "updated_at"]


class PurchasedCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer()
    sub_category = SubcategorySerializer()
    sections = serializers.SerializerMethodField()
    class Meta:
        model = CourseModel
        exclude = ["created_at", "updated_at"]
    def get_sections(self, obj):
        try:
            sec = []
            objs = obj.course_sections.all()
            serializer = SectionWithTopicsSerializer(objs ,many=True)
            sec = serializer.data
            return sec
        except Exception as e:
            print(e)

