from django.db import models

# Create your models here.
class ESTOQUE(models.Model):
    # db_table = 'ESTOQUE'

    codigo = models.CharField(max_length=6, primary_key=True)
    barras = models.CharField(max_length=20)
    descricao = models.CharField(max_length=40)
    und = models.CharField(max_length=40)
    qtd = models.SmallIntegerField()
    preco_venda = models.DecimalField(decimal_places=4, max_digits=15)
    tamanho = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao
    # ao invés de retornar o código, precisamos retornar um nome pra ficar mais fácil de escolher
    # onde está esse "nome"?

    class Meta:
        db_table = 'ESTOQUE'

class Orcamento(models.Model):
    nome_do_cliente = models.CharField('Nome do Cliente', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    telefone = models.IntegerField('Telefone')
    data_do_veiculo = models.DateField("Data do Veículo")
    modelo = models.CharField('Modelo do Veículo', max_length=30)
    placa = models.CharField('Placa de Veículo', max_length=7)
    cpf_cnpj = models.IntegerField('CPF ou CNPJ')
    inscricao = models.CharField('Inscrição Estadual', max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

class Produto(models.Model):
    codigo = models.CharField(max_length=6)
    quantidade = models.DecimalField(decimal_places=4, max_digits=6)
    preco_unitario = models.DecimalField(decimal_places=4, max_digits=15)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='produtos')