from django.conf.urls import url
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^', include('seatime.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]
