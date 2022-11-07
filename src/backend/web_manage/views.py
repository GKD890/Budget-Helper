from django.shortcuts import render
from rest_framework import viewsets
from .sender import MemberSerializer, RecordSerializer
from .models import Member, Record

# Create your views here.

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class RecordView(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()