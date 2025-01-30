from django.contrib import admin
from django.urls import path
from ofertas.views import UniversidadeListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('universidades/', UniversidadeListAPIView.as_view())
]
