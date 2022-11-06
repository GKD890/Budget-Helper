from django.shortcuts import render
from rest_framework import viewsets
from .sender import MemberSerializer
from .models import Member

# Create your views here.

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()