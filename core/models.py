from django.db import models

class Produtos(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    barras = models.CharField(max_length=20)
    descricao = models.CharField(max_length=40)
    und = models.CharField(max_length=40)
    qtd = models.SmallIntegerField()
    preco_venda = models.DecimalField(decimal_places=4, max_digits=15)
    tamanho = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'ESTOQUE'

class Orcamento(models.Model):
    nome_do_cliente = models.CharField('Nome do Cliente', max_length=100)
    endereco = models.CharField('Endereço', max_length=100, null=True, blank=True)
    telefone = models.IntegerField('Telefone')
    veiculo = models.CharField('Modelo do Veículo', max_length=30)
    placa = models.CharField('Placa de Veículo', max_length=7, null=True, blank=True)
    cpf_cnpj = models.IntegerField('CPF ou CNPJ',  null=True, blank=True)
    inscricao = models.CharField('Inscrição Estadual', max_length=30, null=True, blank=True)
    garantia = models.CharField('Garantia', max_length=1000, null=True, blank=True)
    pagamento = models.CharField('Condições de Pagamento', max_length=1000, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Orcamento'

class Orcamento_Produto(models.Model):
    codigo = models.CharField(max_length=6)
    quantidade = models.DecimalField(decimal_places=4, max_digits=6)
    desconto = models.DecimalField(decimal_places=4, max_digits=6, blank=True)
    preco_unitario = models.DecimalField(decimal_places=4, max_digits=15)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='produtos')

    class Meta:
        db_table = 'Orcamento_Produto'