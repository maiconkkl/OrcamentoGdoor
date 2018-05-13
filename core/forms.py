from django import forms
from .models import Orcamento, Orcamento_Produto

class OrcamentoForm(forms.ModelForm):
    nome_do_cliente = forms.CharField(label='Nome do Cliente', max_length=100)
    endereco = forms.CharField(label='Endereço do Cliente', max_length=100, required=False)
    telefone = forms.IntegerField(label='Telefone do Cliente')
    cpf_cnpj = forms.IntegerField(label='CPF ou CNPJ do Cliente', required=False)
    inscricao = forms.CharField(label='Inscrição Estadual do Cliente', max_length=30, required=False)
    veiculo = forms.CharField(label='Modelo do Veículo', max_length=30)
    placa = forms.CharField(label='Placa do Veículo', max_length=7, required=False)
    garantia = forms.CharField(label='Garantia', max_length=1000, required=False)
    pagamento = forms.CharField(label='Condições de Pagamento', max_length=1000)

    class Meta:
        model = Orcamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        orcamento = super(OrcamentoForm, self).save(commit=False)
        orcamento.nome_do_cliente = self.cleaned_data['nome_do_cliente']
        orcamento.endereco = self.cleaned_data['endereco']
        orcamento.telefone = self.cleaned_data['telefone']
        orcamento.cpf_cnpj = self.cleaned_data['cpf_cnpj']
        orcamento.inscricao = self.cleaned_data['inscricao']
        orcamento.veiculo = self.cleaned_data['veiculo']
        orcamento.placa = self.cleaned_data['placa']
        orcamento.garantia = self.cleaned_data['garantia']
        orcamento.pagamento = self.cleaned_data['pagamento']
        orcamento.save()#isso aki ta chamando o modelo
        return orcamento

class ProdutoForm(forms.ModelForm):
    codigo = forms.CharField(max_length=6)
    preco_unitario = forms.DecimalField(decimal_places=4, max_digits=15)
    quantidade = forms.DecimalField(decimal_places=4, max_digits=15)

    class Meta:
        model = Orcamento_Produto
        fields = {}

    def save(self, commit=True):
        produto = super(ProdutoForm, self).save(commit=False)
        produto.codigo = self.cleaned_data['codigo']
        produto.quantidade = self.cleaned_data['quantidade']
        produto.preco_unitario = self.cleaned_data['preco_unitario']
        produto.save()