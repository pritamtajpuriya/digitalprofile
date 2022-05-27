from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import UserRegistrationRequestSerializer, UserLoginRequestSerializer, UserSerializer


USER = get_user_model()


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user

class UserRegistrationRequestCreateAPIView(CreateAPIView):
    """User create"""
    queryset = USER.objects.all()
    serializer_class = UserRegistrationRequestSerializer
    permission_classes = [AllowAny, ]


class UserLoginRequestAPIView(APIView):
    """User login"""
    permission_classes = [AllowAny, ]

    @staticmethod
    def post(request: Request):
        serializer = UserLoginRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        access_token = AccessToken.for_user(user)
        return Response({
            "access": str(access_token),
        })
