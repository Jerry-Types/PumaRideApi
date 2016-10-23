from rest_framework import serializers
from .models import Point
from .models import Line

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields= ('id','name','p_origen','p_destino','shortes_path',)