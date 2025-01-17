from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    full_name = serializers.ReadOnlyField(source="user.full_name")
    country = CountryField(name_only=True)
    date_joined = serializers.DateTimeField(source="user.date_joined", read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "city_of_origin",
            "country",
            "slug",
            "bio",
            "date_joined",
            "gender",
            "reputation",
            "avatar",
        ]

    def get_avatar(self, obj) -> None:
        if obj.user.profile.avatar:
            return obj.user.profile.avatar.url
        return None


class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "username",
            "country",
            "city_of_origin",
            "bio",
            "gender",
            "phone_number",
        ] 


class UploadAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["avatar"]
