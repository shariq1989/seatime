from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import MarinerProfile, MarinerDocument, Vessel, WorkdayType, VoyageType
from .serializers import MarinerProfileSerializer, UserSerializer, MarinerDocumentSerializer, VesselSerializer, \
    WorkdayTypeSerializer, VoyageTypeSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MarinerProfileViewSet(viewsets.ModelViewSet):
    queryset = MarinerProfile.objects.all()
    serializer_class = MarinerProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MarinerDocumentViewSet(viewsets.ModelViewSet):
    queryset = MarinerDocument.objects.all()
    serializer_class = MarinerProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer


class WorkdayTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkdayType.objects.all()
    serializer_class = WorkdayTypeSerializer


class VoyageTypeViewSet(viewsets.ModelViewSet):
    queryset = VoyageType.objects.all()
    serializer_class = VoyageTypeSerializer

class VoyageTypeViewSet(viewsets.ModelViewSet):
    queryset = VoyageType.objects.all()
    serializer_class = VoyageTypeSerializer

class VoyageTypeViewSet(viewsets.ModelViewSet):
    queryset = VoyageType.objects.all()
    serializer_class = VoyageTypeSerializer
