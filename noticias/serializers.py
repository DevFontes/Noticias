from rest_framework_mongoengine import serializers
from .models import Noticia

class NoticiaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
        