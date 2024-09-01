from django.contrib import admin
from .models import Aluno  # Importa o modelo Aluno

@admin.register(Aluno)  # Decorador para registrar o modelo
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'cpf')  # Campos que você deseja exibir na lista
    search_fields = ('nome', 'cpf')  # Campos para os quais você pode pesquisar
