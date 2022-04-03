from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('all-categories/', views.CategoryListView.as_view(), name="all-categories"),
    path('sub-categories/<cat_id>/', views.SubCategoriesView.as_view(), name="sub-categories"),
    path('cources/<cat_id>/', views.CourcesView.as_view(), name="cources"),
    path('cource/<id>/', views.SingleCourceView.as_view(), name="cource"),
]