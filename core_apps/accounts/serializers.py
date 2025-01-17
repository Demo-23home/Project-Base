from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "first_name", "last_name", "password"]


class CustomUserSerializer(UserSerializer):
    phone_number = PhoneNumberField(source="profile.phone_number")
    full_name = serializers.ReadOnlyField(source="profile.full_name")
    gender = serializers.ReadOnlyField(source="profile.gender")
    slug = serializers.ReadOnlyField(source="profile.slug")
    country = CountryField(source="profile.country")
    city = serializers.ReadOnlyField(source="profile.city_of_origin")
    avatar = serializers.SerializerMethodField()
    reputation = serializers.ReadOnlyField(source="profile.reputation")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "date_joined",
            "full_name",
            "phone_number",
            "gender",
            "slug",
            "country",
            "city",
            "avatar",
            "reputation",
        ]

    read_only_fields = ["id", "date_joined", "email"]

    def get_avatar(self, obj) -> None:
        if obj.profile.avatar:
            return obj.profile.avatar.url
        else:
            return None
