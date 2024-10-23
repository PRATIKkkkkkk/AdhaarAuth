from rest_framework import serializers

class AdhaarAuthSerializer(serializers.Serializer):
    adhaar_number = serializers.CharField(max_length=12)
    otp = serializers.CharField(max_length=6, required=False)