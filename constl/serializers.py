from rest_framework import serializers

from .models import ContactEnquiry


class ContactEnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactEnquiry
        fields = [
            "id",
            "name",
            "organisation",
            "email",
            "phone",
            "service",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Name is required."
            )

        return value

    def validate_email(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Email is required."
            )

        return value

    def validate_message(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Message is required."
            )

        return value