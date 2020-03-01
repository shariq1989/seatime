from django.conf.urls import url, include
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mariner-profile/', views.MarinerProfileList.as_view()),
    path('mariner-profile/<int:pk>/', views.MarinerProfileDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
