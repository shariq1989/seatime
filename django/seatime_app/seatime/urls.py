from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mariner-profiles', views.MarinerProfileViewSet, basename='MarinerProfile')
router.register(r'mariner-documents', views.MarinerDocumentViewSet, basename='MarinerDocs')
router.register(r'vessels', views.VesselViewSet, basename='Vessels')
router.register(r'workday-types', views.WorkdayTypeViewSet, basename='WorkdayTypes')
router.register(r'voyage-types', views.VoyageTypeViewSet, basename='VoyageTypes')
router.register(r'ranks', views.RankViewSet, basename='Rank')
router.register(r'voyages', views.VoyageViewSet, basename='Voyages')

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # for adding login to browsable API
    path('api-auth/', include('rest_framework.urls')),
    path('control/', admin.site.urls),
    url(r'^authenticate/', views.CustomObtainAuthToken.as_view()),
]
