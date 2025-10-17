from rest_framework import serializers
from app.crm.models import FieldActivity, ValidationLevel, CallReport


# ─────────────────────────────
# FieldActivity Serializer
# ─────────────────────────────
class FieldActivitySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)

    class Meta:
        model = FieldActivity
        fields = ['id', 'name', 'parent', 'parent_name']


# ─────────────────────────────
# ValidationLevel Serializer
# ─────────────────────────────
class ValidationLevelSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.name', read_only=True)

    class Meta:
        model = ValidationLevel
        fields = ['id', 'name', 'parent', 'parent_name']


# ─────────────────────────────
# CallReport Serializer
# ─────────────────────────────
class CallReportSerializer(serializers.ModelSerializer):
    field_activity = FieldActivitySerializer(read_only=True)
    validation = ValidationLevelSerializer(read_only=True)

    absolute_url = serializers.SerializerMethodField(read_only=True)

   
    field_activity_id = serializers.PrimaryKeyRelatedField(
        source='field_activity', queryset=FieldActivity.objects.all(), write_only=True, required=False
    )
    validation_id = serializers.PrimaryKeyRelatedField(
        source='validation', queryset=ValidationLevel.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = CallReport
        fields = [
            'id', 'number', 'name', 'province', 'city',
            'field_activity', 'field_activity_id',
            'last_purchase', 'purchase_satisfaction',
            'validation', 'validation_id',
            'description', 'created_at', 'updated_at','absolute_url',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_absolute_url(self, obj):
        # Generate absolute URL for the post
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)