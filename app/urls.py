from django.urls import path
from .views import index
from django.conf.urls.static import static, settings

urlpatterns = [
        path('', index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
