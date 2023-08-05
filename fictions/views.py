from django.shortcuts import render
from .models import Fiction
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import FictionSerializer

from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class FictionListView(ListAPIView):
class FictionListView(ListCreateAPIView):

    queryset = Fiction.objects.all()
    serializer_class = FictionSerializer


class FictionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fiction.objects.all()
    serializer_class = FictionSerializer
    permission_classes = [IsOwnerOrReadOnly]


