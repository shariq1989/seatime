from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import MarinerProfile
from .serializers import MarinerProfileSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MarinerProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MarinerProfile.objects.all()
    serializer_class = MarinerProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
