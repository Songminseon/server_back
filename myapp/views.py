from django.shortcuts import render
from rest_framework import generics

from .models import PhoneBook
from .serializers import PhoneSerializer

class ListPhone(generics.ListCreateAPIView):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneSerializer

class DetailPhone(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneSerializer


# Create your views here.
