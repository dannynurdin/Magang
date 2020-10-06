from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index_view, employee_view

urlpatterns = [
    path('', index_view),
    path('employee/', employee_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)