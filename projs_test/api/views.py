from django.shortcuts import render
from django.http import HttpResponse
from api.models import records
from api.serializers import *
from api.permissions import IsOwnerOrReadOnly
# serilizer all kinds

from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import permissions
from rest_framework import viewsets
import logging
import pymysql
# Create your views here.
def Verify(request):
    if request.method == 'POST':
        zone == request.POST['zone']
    if zone !='www.ww':
        return HttpResponse('-1')
    else:
        return HttpResponse('0')
"""
if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = superuser.objects.all()
        for user in users:
            if user.username == username and user.password == password:
                user_list = superuser.objects.all()
                context = {'user_list': user_list}
                return HttpResponse('1')  
        return HttpResponse('-1')
    else:
        return HttpResponse('0')
"""
class RecordsViewSet(viewsets.ModelViewSet):
    queryset = records.objects.all()
    serializer_class = RecordsSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


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
