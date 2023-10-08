from rest_framework import serializers
from . models import Grupo, Activo, Personal

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grupo
        fields="__all__"


class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Activo
        fields="__all__"


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal
        fields="__all__"
