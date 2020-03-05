from django.db import models
from mongoengine import Document, fields

class Noticia(Document):
    #id_noticia = 
    titulo_noticia = fields.StringField(required=True)
    texto_noticia = fields.StringField(required=True)
    data_noticia = fields.DateField(required=False, null=True)
    autor_noticia = fields.StringField(required=True)
    
class Autor(Document):
    #id_autor
    nome_autor = fields.StringField(required=True)
    email_autor = fields.StringField(required=True)
    data_cadastro_autor = fields.DateField(required=False, null=True)
