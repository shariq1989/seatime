import rest_framework.authtoken
from django.conf.urls import url, include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'mariner-profiles', views.MarinerProfileViewSet)
router.register(r'mariner-documents', views.MarinerDocumentViewSet)
router.register(r'vessels', views.VesselViewSet)
router.register(r'workday-types', views.WorkdayTypeViewSet)
router.register(r'voyage-types', views.VoyageTypeViewSet)
router.register(r'staff-positions', views.StaffPositionViewSet)
router.register(r'voyages', views.VoyageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^fetch-auth-token/', obtain_auth_token),
    url(r'^create-user/', views.CreateUserView),
]
