from django.conf.urls import url
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^', include('seatime.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # TODO: Figure out if schema view is really needed and fix the integration issue
    # url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
