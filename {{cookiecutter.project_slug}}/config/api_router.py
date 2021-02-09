from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from {{ cookiecutter.project_slug }}.users.api.views import UserViewSet, GoogleLogin

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
urlpatterns = [
    path("google/", GoogleLogin.as_view(), name='google_login'),
]

app_name = "api"
urlpatterns += router.urls
