from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm

def home(request):
    data={}
    data['now']="Hoje"
    data['transacoes'] = ['t1','t2']
    return render(request,'contas/home.html',data)

def listagem(request):
    data={}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None);
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data = {};
    data['form']=form
    return render(request, 'contas/form.html', data)
def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance = transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data = {};
    data['form']=form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')