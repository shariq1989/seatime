from django.conf.urls import url, include
from django.urls import path

from . import views, admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'mariner-profiles', views.MarinerProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
