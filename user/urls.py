from django.urls import path

from .views import (UserRegistrationRequestCreateAPIView, UserLoginRequestAPIView, UserViewSet)

app_name = 'user'
urlpatterns = [
    path('me', UserViewSet.as_view({'get': 'retrieve'}), #{'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}
         name='current-user'),
    path('register', UserRegistrationRequestCreateAPIView.as_view(), name='token_obtain_pair'),
    path('token', UserLoginRequestAPIView.as_view(), name="token"),
]