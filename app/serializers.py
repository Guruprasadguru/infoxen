from app.models import Lead
from rest_framework import serializers
class Leadserializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields='__all__'