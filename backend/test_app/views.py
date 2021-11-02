from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from test_app.serializers import SportSerializer, TeamSerializer
from test_app.models import Sport, Team

class SportViewSet(ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
