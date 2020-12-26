from django.shortcuts import render

from rest_framework import generics
from projectApp import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.todoModel.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.todoModel.objects.all()
    serializer_class = TodoSerializer