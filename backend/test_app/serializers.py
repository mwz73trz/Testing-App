from rest_framework.serializers import ModelSerializer, StringRelatedField
from test_app.models import Sport, Team

class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name', 'user', 'teams']
        depth = 1

    user = StringRelatedField()

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'