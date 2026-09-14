from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from authentication.permissions import IsSeller
# Create your views here.

class SellerView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSeller]
    def get(self, request):
        return Response(data={"message":"Open endpoint available"}, status=200)

class Close(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(data={"message":"Close endpoint available"}, status=200)