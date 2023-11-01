from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Policy, BypassSheet, BypassSheetField, Standard, Procedure
from .serializers import ScheduleSerializer, PolicySerializer, ProcedureSerializer, StandardSerializer
from .paginations import DocumentPagination


# Create your views here.
class ScheduleViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = BypassSheet.objects.all()
    pagination_class = DocumentPagination
    serializer_class = ScheduleSerializer
    # permission_classes = [IsForMany]


class PolicySerializerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Policy.objects.all()
    pagination_class = DocumentPagination
    serializer_class = PolicySerializer
    # permission_classes = [IsForMany]


class ProcedureSerializerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Procedure.objects.all()
    pagination_class = DocumentPagination
    serializer_class = ProcedureSerializer
    # permission_classes = [IsForMany]


class StandardSerializerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Standard.objects.all()
    pagination_class = DocumentPagination
    serializer_class = StandardSerializer
    # permission_classes = [IsForMany]
