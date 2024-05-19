from rest_framework import serializers
from furnitures.models import Furnitures

class FurnituresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furnitures
        fields = "__all__"