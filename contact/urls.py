from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "contact"

urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # configuracao para mostrar arquivos de media (imagens) durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)