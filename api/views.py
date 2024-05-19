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
from api.serializers import FurnituresSerializer
from furnitures.models import Furnitures

class FurnituresApiViewSet(ModelViewSet):
    queryset = Furnitures.objects.all()
    serializer_class = FurnituresSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("WhatWeDo",)
    pagination_class = LimitOffsetPagination
