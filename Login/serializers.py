from django.contrib.auth.models import User
from rest_framework import routers, serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


