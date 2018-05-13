from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Produtos
from .models import Orcamento
from .models import Orcamento_Produto
from .forms import ProdutoForm, OrcamentoForm
from django.conf.urls.static import static
from django.urls import reverse

def orcamentocreate(request):
    itens = Produtos.objects.using('firebird').all()
    if request.method == 'POST':
        orcamento = OrcamentoForm(request.POST)

        codigo = request.POST.getlist('codigo[]')
        quantidade = request.POST.getlist('quantidade[]')
        desconto = request.POST.getlist('desconto[]')
        preco_unitario = request.POST.getlist('preco_unitario[]')

        context = {'orcamento': orcamento, 'itens': itens}
        if orcamento.is_valid():
            orcamento = orcamento.save()
            for i in range(len(codigo)):
                produto = Orcamento_Produto()
                produto.codigo = codigo[i]
                produto.quantidade = quantidade[i]
                produto.desconto = desconto[i]
                produto.preco_unitario = preco_unitario[i]
                produto.orcamento = orcamento
                produto.save()
            return HttpResponseRedirect(reverse('orcamento', args=(orcamento.id,)))
        else:
            return render(request, 'orcamento/orcamentocreate.html', context)
    else:
        orcamento = OrcamentoForm()
        context = {'orcamento': orcamento, 'itens': itens}
        return render(request, 'orcamento/orcamentocreate.html', context)

def orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)
    produtos = orcamento.produtos.all()
    lista_estoque = []

    total_produto = 0
    total_desconto = 0
    total = 0

    for produto in produtos:
        obj = Produtos.objects.using('firebird').get(codigo=produto.codigo)
        lista_estoque.append({'codigo': produto.codigo,
                             'descricao': obj.descricao,
                             'preco_unitario': produto.preco_unitario,
                             'quantidade': produto.quantidade,
                              'total': produto.preco_unitario * produto.quantidade})
        total_produto = total_produto + produto.preco_unitario * produto.quantidade
        total_desconto = total_desconto + produto.desconto
    total = total_produto - total_desconto

    return render(request, 'orcamento/orcamentoview.html', {
            'orcamento': orcamento,
            'produtos': produtos,
            'lista_estoque': lista_estoque,
            'total_produto':total_produto,
            'total_desconto':total_desconto,
            'total':total
    })

def orcamentolist(request):
    orcamento = Orcamento.objects.all()
    return render(request, 'orcamento/orcamentolist.html', {
            'orcamentos': orcamento,
    })