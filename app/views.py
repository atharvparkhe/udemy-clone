from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from authentication.models import LearnerModel
from base.utils import paginate
from authentication.serializers import emailSerializer
from .serializers import *
from .models import *


# Display Categories
class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

# Display Subcategories
class SubCategoriesView(ListAPIView):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubcategorySerializer
    def list(self, request, cat_id):
        try:
            cat = CategoryModel.objects.get(id=cat_id)
            if not cat:
                return Response({"message":"Invalid Category ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            objs = cat.sub_categories.all()
            ser = self.serializer_class(objs, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Display Courses List
class CourcesView(ListAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = MultiCourcesSerializer
    def list(self, request, cat_id):
        try:
            cat = SubCategoryModel.objects.get(id=cat_id)
            if not cat:
                return Response({"message":"Invalid Sub-Category ID"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            objs = cat.course_sub_category.all()
            ser = self.serializer_class(objs, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Display Single Course
class SingleCourceView(RetrieveAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"

# Display Purchased Course
class PurchasedCourseView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CourseModel.objects.all()
    serializer_class = PurchasedCourseSerializer
    lookup_field = "id"

# Show Purchased Cources
class ShowPurchasedCourses(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CourseModel.objects.all()
    serializer_class = MultiCourcesSerializer
    # def get_queryset(self):
    #     user = LearnerModel.objects.get(email=self.request.email)
    #     if not user:
    #         return []
    #     return OrderModel.objects.filter(owner=user)
    

