from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from .models import Noticia, Autor
from .serializers import NoticiaSerializer, AutorSerializer

class NoticiaView(APIView):
    #authentication_classes = (SessionAuthentication)
    #permission_classes = (IsAuthenticated,)

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
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        noticia = get_object_or_404(Noticia.objects.all(), pk=pk)
        noticia.delete()
        return Response({"mensagem": f"Deletado ID {pk}"}, status=status.HTTP_200_OK)

    def update(self, request):
        pk = request.data.id
        data = get_object_or_404(Noticia.object.all(), pk=pk)

class AutorView(APIView):
    def get(self, request):
        serializer = AutorSerializer(Autor.objects.all(), many=True)
        response = {"autores": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = AutorSerializer(data=data)
        if serializer.is_valid():
            autor = Autor(**data)
            autor.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            
