from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Noticia
from .serializers import NoticiaSerializer

class NoticiaView(APIView):

    def get(self, request):
        serializer = NoticiaSerializer(Noticia.objects.all(), many=True)
        response = {"noticias": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        data = request.data
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            noticia = Noticia(**data)
            noticia.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)


