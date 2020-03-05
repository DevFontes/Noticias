from django.db import models
from mongoengine import Document, fields, EmbeddedDocument, EmbeddedDocumentField

class Noticia(EmbeddedDocument):
    titulo_noticia = fields.StringField(required=True)
    texto_noticia = fields.StringField(required=True)
    data_noticia = fields.DateField(required=False, null=True)
    #autor_noticia = fields.StringField(required=True)
    
class Autor(Document):
    nome_autor = fields.StringField(required=True)
    email_autor = fields.StringField(required=True)
    data_cadastro_autor = fields.DateField(required=False, null=True)
    noticias = fields.ListField(EmbeddedDocumentField(Noticia))
