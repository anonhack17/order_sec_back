from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'logo',
            'company',
            'name',
            'leader',
            'created_at',
            'updated_at',
            'policy',
            'standard',
            'procedure',
            'bpassSheet',
        ]



class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'logo',
            'company',
            'name',
            'leader',
            'created_at',
            'updated_at',
            'policy',
            'standard',
            'procedure',
            'bpassSheet',
        ]
