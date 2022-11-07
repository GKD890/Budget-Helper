from rest_framework import serializers
from .models import Member, Record

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name','id','borrow','lend')

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('person','other_person','borrow','lend','repay','trans_date','complete','description')