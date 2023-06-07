from rest_framework import routers,serializers,viewsets
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'full_name', 'email', 'password']

class PersonSerializer_Without_PWD(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['full_name', 'email']