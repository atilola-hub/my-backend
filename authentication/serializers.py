from rest_framework import serializers
from authentication.models import ACCOUNT_TYPES
class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fullname = serializers.CharField(max_length=255)
    phone = serializers.CharField()
    address = serializers.CharField()
    bvn = serializers.CharField()
    type = serializers.ChoiceField(choices=[x[0] for x in ACCOUNT_TYPES])
    password = serializers.CharField()
    dob = serializers.DateField()
    def validate(self, attr):
        phone = attr["phone"]
        if not phone.startswith("+234"):
            raise serializers.ValidationError("Phone number must start with +234")
        if len(phone) != 14:
            raise serializers.ValidationError("Phone number must be exactly 14 characters")
        try:
            int(phone[1:])
        except:
            raise serializers.ValidationError("Phone number must be digits only")

        bvn = attr["bvn"]
        if len(bvn) != 11:
            raise serializers.ValidationError("Bvn must be 11 character long")
        try:
            int(bvn)
        except:
            raise serializers.ValidationError("BVN must only contain numbers")
        password = attr["password"]
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 character long")

        return attr

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()