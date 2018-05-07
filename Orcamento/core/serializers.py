from rest_framework import serializers
from .models import ESTOQUE

class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ESTOQUE
        fields = (
            'codigo',
            'barras',
            'descricao',
            'und',
            'qtd',
            'preco_venda',
            'tamanho',
        )