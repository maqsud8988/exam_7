from rest_framework import serializers
from about.models import Service
from contact.models import Contact
from furnitures.models import Furnitures
from testimonial.models import Testimonial

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class FurnituresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furnitures
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


