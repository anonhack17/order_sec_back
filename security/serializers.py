from rest_framework import serializers
from .models import Policy, BypassSheet, BypassSheetField, Standard, Procedure


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    bypass_sheet_field = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = BypassSheet
        # fields = '__all__'
        fields = ['id','title', 'text1', 'bypass_sheet_field' , 'text2','created_at' ]

