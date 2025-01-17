
from django.urls import path
from .views import (
    AvatarUploadAPIView,
    ProfileListAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="profile-list"),
    path("user/my-profile/", ProfileDetailAPIView.as_view(), name="profile-detail"),
    path("user/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    path("user/avatar/", AvatarUploadAPIView.as_view(), name="avatar-upload"),
]
