from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import MarinerProfile, MarinerDocument, Vessel, WorkdayType, VoyageType, StaffPosition, Voyage, \
    StaffRatingCombinations, Album
from .serializers import MarinerProfileSerializer, UserSerializer, MarinerDocumentSerializer, VesselSerializer, \
    WorkdayTypeSerializer, VoyageTypeSerializer, StaffPositionSerializer, VoyageSerializer, \
    MarinerProfileNoIdSerializer, MarinerDocumentNoIdSerializer, StaffRatingCombinationsSerializer, AlbumSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


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
    serializer_class = MarinerProfileNoIdSerializer

    action_serializers = {
        'list': MarinerProfileSerializer,
        'retrieve': MarinerProfileSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(MarinerProfileViewSet, self).get_serializer_class()

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return MarinerProfile.objects.filter(user=self.request.user)


class MarinerDocumentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = MarinerDocumentNoIdSerializer

    action_serializers = {
        'list': MarinerDocumentSerializer,
        'retrieve': MarinerDocumentSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(MarinerDocumentViewSet, self).get_serializer_class()

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return MarinerDocument.objects.filter(user=self.request.user)


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


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class VoyageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Voyage.objects.filter(user=self.request.user)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
