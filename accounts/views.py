from django.shortcuts import render
from rest_framework import generics 
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import *
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "کاربر با موفقیت ثبت شد."
        }, status=status.HTTP_201_CREATED)



class TokenVerifyView(APIView):
    """
    this view is for verifying the tokens using GET request
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        auth = JWTAuthentication()

        try:
            token = request.headers.get('Authorization').split(' ')[1]
            auth.get_validated_token(token)
            return Response({"message": "توکن معتبر است"}, status=status.HTTP_200_OK)
        except (InvalidToken, AttributeError):
            return Response({"message": "توکن معتبر نیست یا کاربر موجود نیست"}, status=status.HTTP_401_UNAUTHORIZED)