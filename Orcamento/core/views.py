from django.shortcuts import render
from .models import ESTOQUE
from .models import Produto
from .models import Orcamento
from .forms import ProdutoForm, OrcamentoForm
from django.conf.urls.static import static

def orcamentocreate(request):
    itens = ESTOQUE.objects.using('firebird').all()
    if request.method == 'POST':
        orcamento = OrcamentoForm(request.POST)

        codigo = request.POST.getlist('codigo[]')
        quantidade = request.POST.getlist('quantidade[]')
        preco_unitario = request.POST.getlist('preco_unitario[]')

        context = {'orcamento': orcamento, 'itens': itens}
        if orcamento.is_valid():
            orcamento = orcamento.save()
            for i in range(len(codigo)):
                produto = Produto()
                produto.codigo = codigo[i]
                produto.quantidade = quantidade[i]
                produto.preco_unitario = preco_unitario[i]
                produto.orcamento = orcamento
                produto.save()
                print(produto.codigo)
                print(produto.orcamento)
            return render(request, 'core/orcamentocreate.html', context)
        else:
            return render(request, 'core/orcamentocreate.html', context)
    else:
        print('metodo GET')
        orcamento = OrcamentoForm()
        context = {'orcamento': orcamento, 'itens': itens}
        return render(request, 'core/orcamentocreate.html', context)

def orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)
    produtos = orcamento.produtos.all()
    lista_estoque = []
    total = 0
    for produto in produtos:
        obj = ESTOQUE.objects.using('firebird').get(codigo=produto.codigo)

        lista_estoque.append({'codigo': produto.codigo,
                             'descricao': obj.descricao,
                             'preco_unitario': produto.preco_unitario,
                             'quantidade': produto.quantidade,
                              'total': produto.preco_unitario * produto.quantidade})
        total = total + produto.preco_unitario * produto.quantidade


    return render(request, 'core/orcamentoview.html', {
            'orcamento': orcamento,
            'produtos': produtos,
            'lista_estoque': lista_estoque,
            'total':total
    })
def orcamentolist(request):
    orcamento = Orcamento.objects.all()
    return render(request, 'core/orcamentolist.html', {
            'orcamentos': orcamento,
    })