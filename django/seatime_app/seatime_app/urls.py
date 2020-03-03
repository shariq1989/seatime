from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^', include('seatime.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
