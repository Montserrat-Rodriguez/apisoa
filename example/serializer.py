from rest_framework import routers, serializers
from example.models import Carrera
from example.models import Alumnos

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('__all__')
        #fields = ('__all__')

class AlumnosSerializer(serializers.ModelSerializer):
    carrera = serializers.ReadOnlyField(source='carrera_id.nombre')
    class Meta:
        model = Alumnos
        fields = ('__all__')




