
from django.shortcuts import render
from authentication.serializers import SignupSerializer, LoginSerializer
from authentication.models import User
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
# Create your views here.

class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email").lower()
        fullname = serializer.validated_data.get("fullname")
        phone = serializer.validated_data.get("phone")
        address = serializer.validated_data.get("address")
        bvn = serializer.validated_data.get("bvn")
        password = serializer.validated_data.get("password")
        dob = serializer.validated_data.get("dob")
        type = serializer.validated_data.get("type")
        email_exists = User.objects.filter(email=email).first()
        if email_exists:
            return Response(data={"message": "email already exists"}, status=400)
        phone_exists = User.objects.filter(phone=phone).first()
        if phone_exists:
            return Response(data={"message": "phone number already exists"}, status=400)
        user = User.objects.create(
            email = email,
            fullname = fullname,
            phone = phone,
            address = address,
            bvn = bvn,
            dob = dob,
            type = type
        )
        user.set_password(password)
        user.save()
        return Response(data={"message": "success"}, status=201)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email").lower()
        password = serializer.validated_data.get("password")
        email_exists = User.objects.filter(email=email).first()
        if not email_exists:
            return Response({"message":"Invalid credentials"}, status=400)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({"message":"Invalid credentials"}, status=400)
        tokens = user.token()
        return Response(
            data= {
                "id": str(user.id),
                "email": str(user.email),
                "is_active": user.is_active,
                "phone": user.phone,
                "fullname": user.fullname,
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"]
            }
        )
        
