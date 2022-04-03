from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import *
from .threads import *
from .serializers import *
import random


@api_view(["POST"])
def signUp(request):
    try:
        data = request.data
        serializer = signupSerializer(data=data)
        if serializer.is_valid():
            name = serializer.data["name"]
            email = serializer.data["email"]
            password = serializer.data["password"]
            if LearnerModel.objects.filter(email=email).first():
                return Response({"message":"Acount already exists."}, status=status.HTTP_406_NOT_ACCEPTABLE)
            new_user = LearnerModel.objects.create(email=email, name=name)
            new_user.set_password(password)
            new_user.save()
            return Response({"message":"Account created, verification mail sent"}, status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def logIn(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            user_obj = LearnerModel.objects.filter(email=email).first()
            if user_obj is None:
                return Response({"message":"Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user = authenticate(email=email, password=password)
            if not user:
                return Response({"message":"Incorrect password"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            jwt_token = RefreshToken.for_user(user)
            return Response({"message":"Login successfull", "token":str(jwt_token.access_token)}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def forgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            user_obj = LearnerModel.objects.filter(email=email).first()
            if not user_obj:
                return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            otp = random.randint(100001, 999999)
            user_obj.otp = otp
            thread_obj = send_forgot_otp(user_obj.email, otp)
            thread_obj.start()
            user_obj.save()
            return Response({"message":"reset mail sent"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def reset(request):
    try:
        data = request.data
        serializer = otpSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            user_obj = LearnerModel.objects.get(otp=otp)
            if not user_obj:
                return Response({"message":"user does not exist"}, status=status.HTTP_404_NOT_FOUND)
            pw = serializer.data["pw"]
            cpw = serializer.data["cpw"]
            if pw == cpw:
                user_obj.set_password(cpw)
                user_obj.otp = 0
                user_obj.save()
                return Response({"message":"Password changed successfull"}, status=status.HTTP_202_ACCEPTED)
            return Response({"message":"passwords dont match"}, status=status.HTTP_409_CONFLICT)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


########################################################################################################################


@api_view(["POST"])
def teacherSignUp(request):
    try:
        data = request.data
        serializer = signupSerializer(data=data)
        if serializer.is_valid():
            name = serializer.data["name"]
            email = serializer.data["email"]
            password = serializer.data["password"]
            if TeacherModel.objects.filter(email=email).first():
                return Response({"message":"Acount already exists."}, status=status.HTTP_406_NOT_ACCEPTABLE)
            otp = random.randint(100001, 999999)
            new_teacher = TeacherModel.objects.create(email=email, name=name, otp=otp)
            new_teacher.set_password(password)
            thread_obj = send_verification_email(email, otp)
            thread_obj.start()
            new_teacher.save()
            return Response({"message":"Account created, verification mail sent"}, status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def teacherVerify(request):
    try:
        data = request.data
        serializer = otpSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            user_obj = TeacherModel.objects.get(otp=otp)
            if user_obj:
                if user_obj.is_verified:
                    return Response({"message":"Account is already verified"}, status=status.HTTP_412_PRECONDITION_FAILED)
                user_obj.is_verified = True
                user_obj.otp = 0
                user_obj.save()
                return Response({"message":"Account verification successfull"}, status=status.HTTP_202_ACCEPTED)
            return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def teacherLogIn(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            teacher_obj = TeacherModel.objects.filter(email=email).first()
            if teacher_obj is None:
                return Response({"message":"Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
            if not teacher_obj.is_verified:
                return Response({"message":"Email not verified. Check your mail"}, status=status.HTTP_401_UNAUTHORIZED)
            user = authenticate(email=email, password=password)
            if not user:
                return Response({"message":"Incorrect password"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            jwt_token = RefreshToken.for_user(user)
            return Response({"message":"Login successfull", "token":str(jwt_token.access_token)}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def teacherForgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            user_obj = TeacherModel.objects.filter(email=email).first()
            if not user_obj:
                return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            if user_obj.is_verified == False:
                return Response({"message":"Account not verified"}, status=status.HTTP_412_PRECONDITION_FAILED)
            otp = random.randint(100001, 999999)
            user_obj.otp = otp
            thread_obj = send_forgot_otp(user_obj.email, otp)
            thread_obj.start()
            user_obj.save()
            return Response({"message":"reset mail sent"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def teacherReset(request):
    try:
        data = request.data
        serializer = otpSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            user_obj = TeacherModel.objects.get(otp=otp)
            if not user_obj:
                return Response({"message":"user does not exist"}, status=status.HTTP_404_NOT_FOUND)
            pw = serializer.data["pw"]
            cpw = serializer.data["cpw"]
            if pw == cpw:
                user_obj.set_password(cpw)
                user_obj.otp = 0
                user_obj.save()
                return Response({"message":"Password changed successfull"}, status=status.HTTP_202_ACCEPTED)
            return Response({"message":"passwords dont match"}, status=status.HTTP_409_CONFLICT)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def teacherResendVerify(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            user_obj = TeacherModel.objects.get(email=email)
            if not user_obj:
                return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            if user_obj.is_verified:
                return Response({"message":"Account is already verified"}, status=status.HTTP_200_OK)
            otp = random.randint(100001, 999999)
            user_obj.otp = otp
            thread_obj = send_verification_email(user_obj.email, otp)
            thread_obj.start()
            user_obj.save()
            return Response({"message":"OTP sent on your email"}, status=status.HTTP_200_OK)
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

