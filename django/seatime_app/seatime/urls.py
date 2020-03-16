from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mariners', views.UserViewSet)
router.register(r'mariner-profiles', views.MarinerProfileViewSet)
router.register(r'mariner-documents', views.MarinerDocumentViewSet)
router.register(r'vessels', views.VesselViewSet)
router.register(r'workday-types', views.WorkdayTypeViewSet)
router.register(r'voyage-types', views.VoyageTypeViewSet)
router.register(r'staff-positions', views.StaffPositionViewSet)
router.register(r'voyages', views.VoyageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('control/', admin.site.urls),
]
