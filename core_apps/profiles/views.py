from typing import List
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework import filters, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from core_apps.common.renderers import GenericJsonRenderer
from .models import Profile
from .serializers import UploadAvatarSerializer, ProfileSerializer, UpdateProfileSerializer
from .tasks import upload_avatar_to_cloudinary


User = get_user_model()


class StandardResultSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "page_size"
    max_page_size = 100


class ProfileListAPIView(generics.ListAPIView):
    renderer_classes = [GenericJsonRenderer]
    serializer_class = ProfileSerializer
    pagination_class = StandardResultSetPagination
    object_label = "profiles"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["user__username", "user__last_name", "user__first_name", "user__email"]
    filterset_fields = ["city_of_origin", "gender"]

    def get_queryset(self) -> List[Profile]:
        excluded_admin_profiles = Profile.objects.exclude(user__is_staff=True).exclude(user__is_superuser=True)

        return excluded_admin_profiles


class ProfileDetailAPIView(generics.RetrieveAPIView):
    renderer_classes = [GenericJsonRenderer]
    serializer_class = ProfileSerializer
    object_label = "profile"

    def get_queryset(self) -> Profile:
        user_profile = Profile.objects.select_related("user").all()

        return user_profile

    def get_object(self) -> Profile:
        user = self.request.user
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise Http404("Profile for such user not found!")

        return user_profile


class ProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateProfileSerializer
    renderer_classes = [GenericJsonRenderer]
    object_label = "profile"

    def get_queryset(self) -> None:
        return Profile.objects.none()

    def get_object(self) -> Profile:
        user = self.request.user
        user_profile, _ = Profile.objects.get_or_create(user=user)
        return user_profile

    def perform_update(self, serializer: UpdateProfileSerializer) -> Profile:
        user = self.request.user
        user_data = serializer.validated_data.pop("user", {})
        profile = serializer.save()
        
        User.objects.filter(id=user.id).update(**user_data)
        return profile
    
    
class AvatarUploadAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        return self.upload_avatar(request, *args, **kwargs)

    def upload_avatar(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = UploadAvatarSerializer(profile, data=request.data)

        if serializer.is_valid():
            image = serializer.validated_data["avatar"]

            image_content = image.read()

            upload_avatar_to_cloudinary.delay(str(profile.id), image_content)

            return Response({"message": "Avatar upload started."}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)