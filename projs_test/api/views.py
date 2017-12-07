from django.shortcuts import render
from api.models import records
from api.serializers import *
from api.permissions import IsOwnerOrReadOnly
# serilizer all kinds
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import filters
import logging
import pymysql
# Create your views here.
class RecordsViewSet(viewsets.ModelViewSet):
    queryset = records.objects.all()
    serializer_class = RecordsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields =('$zone', '$host','$type', '$data','$serial')
    ordering_fields = ('id', 'reg_time')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRegis(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializers
    permission_classes =(AllowAny,)
    def post(self, request, format = None):
        data = request.data
        username = data
        if User.objects.filter(username__exact=username):
            return Response("用户名已存在",HTTP_400_BAD_REQUEST)
        serializer = UserRegSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	   


class RecordsList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = records.objects.all()
    serializer_class = RecordsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user) 

class RecordsDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    qureyset = records.objects.all()
    serializer_class = RecordsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
 
 
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializers


class UserDetail(generics.RetrieveAPIView):
    queryset   =  User.objects.all()
    serializer_class = UserSerializers
