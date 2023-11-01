from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ScheduleViewSet, ProcedureSerializerViewSet, PolicySerializerViewSet, StandardSerializerViewSet

router = DefaultRouter()

router.register('security/schedule', ScheduleViewSet)
router.register('security/procedure', ProcedureSerializerViewSet)
router.register('security/policy', PolicySerializerViewSet)
router.register('security/standard', StandardSerializerViewSet)

