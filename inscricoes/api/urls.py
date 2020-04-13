from django.urls import path, include


urlpatterns = [
    path("v1/", include("inscricoes.api.v1.urls")),
]
