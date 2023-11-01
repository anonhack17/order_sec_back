from rest_framework import serializers

from customer.serializers import CustomerSerializer
from .models import Company


class CompanyListSerializer(serializers.ModelSerializer):
    # customer = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # products = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    # customer = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # products = serializers.SlugRelatedField(slug_field='name',many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
