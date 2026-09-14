from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "fullname", "phone",
                  "address","bvn", "type", "dob"]
        read_only_fields = ["id", "email"]
    def validate(self, attr):
        phone = attr.get("phone")
        if phone:
            if not phone.startswith("+234"):
                raise serializers.ValidationError("Phone number must start with +234")
            if len(phone) != 14:
                raise serializers.ValidationError("Phone number must be exactly 14 characters")
            try:
                int(phone[1:])
            except:
                raise serializers.ValidationError("Phone number must be digits only")
    
        bvn = attr.get("bvn")
        if bvn:
            if len(bvn) != 11:
                raise serializers.ValidationError("Bvn must be 11 character long")
            try:
                int(bvn)
            except:
                raise serializers.ValidationError("BVN must only contain numbers")
    
        return attr