from rest_framework import serializers
from app.accounts.models import User, UserType

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField(read_only=True)
    type = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "id",
            "phone_number",
            "first_name",
            "last_name",
            "full_name",
            "type",
            "is_active",
            "is_verified",
            "created_date",
            "updated_date",
            "absolute_url",
        ]
        read_only_fields = ["id", "created_date", "updated_date", "full_name"]

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        view = self.context.get('view')
        if view and hasattr(view, 'action') and view.action == 'retrieve':
            rep.pop('absolute_url', None)
        return rep

    def get_type(self, obj):
        return {
            "id": obj.type,
            "label": obj.get_type_display(), 
            "name": UserType(obj.type).name
        }

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        model = User
        fields = ["phone_number", "first_name", "last_name", "password", "type"]

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data["phone_number"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            type=validated_data.get("type", UserType.KARSHENAS_FOROOSH),
        )
        return user