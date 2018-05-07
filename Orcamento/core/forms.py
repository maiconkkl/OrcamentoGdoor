from django import forms
from .models import Produto, Orcamento

class OrcamentoForm(forms.ModelForm):
    nome_do_cliente = forms.CharField(max_length=100, label='Nome do Cliente')
    endereco = forms.CharField(max_length=100, label='Endereço do Cliente')
    telefone = forms.IntegerField(label='Telefone do Cliente')
    cpf_cnpj = forms.IntegerField(label='CPF ou CNPJ do Cliente')
    inscricao = forms.CharField(label='Inscrição Estadual do Cliente', max_length=30)
    data_do_veiculo = forms.DateField(label='Data do Veículo')
    modelo = forms.CharField(max_length=30, label='Modelo do Veículo')
    placa = forms.CharField(max_length=7, label='Placa do Veículo')

    class Meta:
        model = Orcamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)
        self.fields['data_do_veiculo'].widget.attrs['class']= 'form-control'

    def save(self, commit=True):
        orcamento = super(OrcamentoForm, self).save(commit=False)
        orcamento.nome_do_cliente = self.cleaned_data['nome_do_cliente']
        orcamento.endereco = self.cleaned_data['endereco']
        orcamento.telefone = self.cleaned_data['telefone']
        orcamento.cpf_cnpj = self.cleaned_data['cpf_cnpj']
        orcamento.inscricao = self.cleaned_data['inscricao']
        orcamento.data_do_veiculo = self.cleaned_data['data_do_veiculo']
        orcamento.modelo = self.cleaned_data['modelo']
        orcamento.placa = self.cleaned_data['placa']
        orcamento.save()#isso aki ta chamando o modelo
        return orcamento


class ProdutoForm(forms.ModelForm):
    codigo = forms.CharField(max_length=6)
    preco_unitario = forms.DecimalField(decimal_places=4, max_digits=15)
    quantidade = forms.DecimalField(decimal_places=4, max_digits=15)

    class Meta:
        model = Produto
        fields = {}

    def save(self, commit=True):
        produto = super(ProdutoForm, self).save(commit=False)
        produto.codigo = self.cleaned_data['codigo']
        produto.quantidade = self.cleaned_data['quantidade']
        produto.preco_unitario = self.cleaned_data['preco_unitario']
        produto.save()