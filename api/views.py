from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from api.serializers import FurnituresSerializer, AboutSerializer, ContactSerializer, TestimonialSerializer
from about.models import Service
from furnitures.models import Furnitures
from rest_framework import serializers
from contact.models import Contact
from testimonial.models import Testimonial



class AboutApiViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("AboutOurCarService",)
    pagination_class = LimitOffsetPagination


class ContactApiViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("full_name",)
    pagination_class = LimitOffsetPagination


class FurnituresApiViewSet(ModelViewSet):
    queryset = Furnitures.objects.all()
    serializer_class = FurnituresSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("WhatWeDo",)
    pagination_class = LimitOffsetPagination


class TestimonialApiViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    pagination_class = LimitOffsetPagination

