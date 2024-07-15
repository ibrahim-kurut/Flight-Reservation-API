from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, UserSerializer

from .permissions import IsAdminOnly


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


     # for return created successfully message
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = {
            "message": "your account registered successfully",
            }
        return Response(
            {
                "message":message,

                "data":serializer.data
                }, 
                status=status.HTTP_201_CREATED, headers=headers
                )



# get all users
class UsersInfo(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]