from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('signup/', views.signUp, name="signup"),
	path('login/', views.logIn, name="login"),
	path('forgot/', views.forgot, name="forgot"),
	path('reset/', views.reset, name="reset"),
    
	path('teacher-signup/', views.teacherSignUp, name="teacher-signup"),
	path('teacher-verify/', views.teacherVerify, name="teacher-verify"),
	path('teacher-login/', views.teacherLogIn, name="teacher-login"),
	path('teacher-forgot/', views.teacherForgot, name="teacher-forgot"),
	path('teacher-reset/', views.teacherReset, name="teacher-reset"),
    path('teacher-resend-verify/', views.teacherResendVerify, name="teacher-resend-verify"),
]