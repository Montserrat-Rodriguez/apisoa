from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from Login.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404

import time

#IsAuthenticated


from example.models import Alumnos
from example.models import Carrera

from example.serializer import AlumnosSerializer
from example.serializer import CarreraSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CarreraList(APIView):
    
    def get(self, request, format=None):
        queryset = Carrera.objects.all()
        serializer = CarreraSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarreraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CarreraDetail(APIView):
    def get_object(self, id):
        try:
            return Carrera.objects.get(pk=id)
        except Carrera.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = CarreraSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Carrera.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = CarreraSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarreraListAll(APIView):
    def get(self, request, format=None):
        queryset = Carrera.objects.all()
        serializer = CarreraviewSerializer(queryset, many=True)
        return Response(serializer.data)
         

#//////////////////////////////////////////////////////////////////////////////////////////////

class AlumnosList(APIView):    
    def get(self, request, format=None):
        queryset = Alumnos.objects.all()
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnostListNombre(APIView):
    def get(self, request, nombre1, format=None):
        queryset = Alumnos.objects.filter(nombre=nombre1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListEdad(APIView):
    def get(self, request, edad1, format=None):
        queryset = Alumnos.objects.filter(edad=edad1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListCarrera(APIView):
    def get(self, request, carrera1, format=None):
        queryset = Alumnos.objects.filter(carrera_id=carrera1)
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnostListAll(APIView):
    def get(self, request, format=None):
        queryset = Alumnos.objects.filter()
        serializer = AlumnosSerializer(queryset, many=True)
        return Response(serializer.data)

class AlumnosDetail(APIView):
    def get_object(self, id):
        try:
            return Alumnos.objects.get(pk=id)
        except Alumnos.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = AlumnosSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumnos.objects.get(pk=id).delete()
        return Response("ok") 
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = AlumnosSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#//////////////////////////////////////////////////////////////////////////////////////////////

class UsersList(APIView):
    
    def get(self, request, format=None):
        if request.data['Token'] == "0":
            return Response("No está logeado")
        else:    
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, context={'request': request}, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            user = User.objects.create_user(request.data['username'], '', request.data['password'])
            if request.data['is_superuser'] == 'true':
                user.is_superuser = True
            else:
                user.is_superuser = False
            user.save()
            #serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,
        context = {'request':request}) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })







