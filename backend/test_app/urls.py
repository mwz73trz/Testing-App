from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test_app.views import SportViewSet, TeamViewSet

router = DefaultRouter()
router.register("sports", SportViewSet, basename="sport")
router.register("teams", TeamViewSet, basename="team")

urlpatterns = [
    path('', include(router.urls)),
]