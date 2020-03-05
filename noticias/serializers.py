from rest_framework_mongoengine import serializers
from .models import Noticia, Autor

class NoticiaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
        
class AutorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        