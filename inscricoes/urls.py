from django.urls import path, include

from .views import index


urlpatterns = [
    path("api/", include("inscricoes.api.urls")),
]
