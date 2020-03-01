from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from django.seatime_app.seatime.models import MarinerProfile
from django.seatime_app.seatime.serializers import MarinerProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MarinerProfileList(generics.ListCreateAPIView):
    queryset = MarinerProfile.objects.all()
    serializer_class = MarinerProfileSerializer


class MarinerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarinerProfile.objects.all()
    serializer_class = MarinerProfileSerializer
