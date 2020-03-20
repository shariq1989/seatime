from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView

from .models import MarinerProfile, MarinerDocument, Vessel, WorkdayType, VoyageType, StaffPosition, Voyage
from .serializers import MarinerProfileSerializer, UserSerializer, MarinerDocumentSerializer, VesselSerializer, \
    WorkdayTypeSerializer, VoyageTypeSerializer, StaffPositionSerializer, VoyageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MarinerProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MarinerProfile.objects.all()
    serializer_class = MarinerProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MarinerDocumentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MarinerDocument.objects.all()
    serializer_class = MarinerDocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VesselViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer


class WorkdayTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = WorkdayType.objects.all()
    serializer_class = WorkdayTypeSerializer


class VoyageTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = VoyageType.objects.all()
    serializer_class = VoyageTypeSerializer


class StaffPositionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = StaffPosition.objects.all()
    serializer_class = StaffPositionSerializer


class VoyageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
