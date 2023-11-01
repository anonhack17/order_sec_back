
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProjectViewSet

router = DefaultRouter()

router.register('project/project', ProjectViewSet)