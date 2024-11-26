from django.contrib import admin
from app_cad_usuarios.models import Usuario, EmailSubscription
from django import forms
# Register your models here.

class EmailsCadastrados(admin.ModelAdmin):
    def get_usuario_email(self, obj):
        return obj.usuario.emailsubscription.email

    def get_usuario_data(self, obj):
        return obj.usuario.emailsubscription.updated_at
    
    # Exibe os campos diretamente do modelo EmailSubscription
    list_display = ('email', 'updated_at')

class Usuarios(admin.ModelAdmin):
    def get_usuario_id_usuario(self, obj):
        return obj.usuario.usuario.id_usuario

    def get_usuario_nome(self, obj):
        return obj.usuario.usuario.nome
    
    def get_usuario_idade(self, obj):
        return obj.usuario.usuario.idade    
    
    # Exibe os campos diretamente do modelo EmailSubscription
    list_display = ('id_usuario', 'nome', 'idade')

admin.site.register(Usuario, Usuarios) 
admin.site.register(EmailSubscription, EmailsCadastrados)    