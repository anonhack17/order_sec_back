from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CompanyViewSet

router = DefaultRouter()

router.register('company/company', CompanyViewSet)