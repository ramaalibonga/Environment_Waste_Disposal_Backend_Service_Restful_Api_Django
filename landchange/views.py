from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Landchange,Admin,Comment,Address
from .serializer import CreateLandViewSerializer,\
RetriveLandchangeViewSerializer,\
RetrieveUpdateDestroyLandchangeViewSerializer,CreateAdminSerializer,AdminUserSerializer,\
AdminUserRetrieveUpdateDestroySerializer,CreateCommentSerializer,CommentSerializer,CommentRetrieveUpdateDestroySerializer,\
CreateAddressSerializer

class CreateLandChangeView(generics.CreateAPIView):
        queryset = Landchange.objects.all()
        serializer_class = CreateLandViewSerializer 
        permission_classes = (IsAuthenticated,)

class RetriveLandchangeView(generics.ListAPIView):
        queryset = Landchange.objects.all()
        serializer_class = RetriveLandchangeViewSerializer
        filter_backends = [filters.DjangoFilterBackend]
        filterset_fields = ['remark']
        search_fields = ['remark']


class RetriveUpdateDestroyLandchangeView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Landchange.objects.all()
        serializer_class = RetrieveUpdateDestroyLandchangeViewSerializer
        permission_classes = (IsAuthenticated,)

class CreateAdminView(generics.CreateAPIView):
       queryset = Admin.objects.all()
       serializer_class = CreateAdminSerializer
       permission_classes = (IsAuthenticated,)

class AdminUserView(generics.ListAPIView):
       queryset = Admin.objects.all()
       serializer_class = AdminUserSerializer
       filter_backends = [filters.DjangoFilterBackend]
       filterset_fields = ['first_name']
       search_fields = ['last_name']

class AdminUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Admin.objects.all()
       serializer_class = AdminUserRetrieveUpdateDestroySerializer
       permission_classes = (IsAuthenticated,)

class CreateCommentView(generics.CreateAPIView):
       queryset = Comment.objects.all()
       serializer_class = CreateCommentSerializer
       permission_classes = (IsAuthenticated,)

class CommentView(generics.ListAPIView):
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
       queryset = Comment.objects.all()
       serializer_class = CommentRetrieveUpdateDestroySerializer
       permission_classes = (IsAuthenticated,)

class CreateAddressView(generics.CreateAPIView):
       queryset = Address.objects.all()
       serializer_class = CreateAddressSerializer
       permission_classes = (IsAuthenticated,)

# class AddressView(generics.ListAPIView):
#        queryset = Address.objects.all()
#        serializer_class = RetrieveAddressViewserializer

     
       
      
