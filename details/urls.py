from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, upload,
    more
)

urlpatterns = [
    path('', home, name = 'home'),
    path('upload/', upload, name = 'upload'),
    path('more/', more, name = 'more')
]+ static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
