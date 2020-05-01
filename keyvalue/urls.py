from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from . import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='KeyValue Api')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include(('keyvalue_app.urls', 'api',), namespace='api'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
