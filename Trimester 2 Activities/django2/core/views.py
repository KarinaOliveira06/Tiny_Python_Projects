from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Conta, Movimentacao
from .forms import OperacaoForm

def detalhe_conta(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
    movimentacoes = conta.movimentacoes.all().order_by('-data_hora')
    
    return render(request, 'core/detalhe_conta.html', {'conta': conta, 'movimentacoes': movimentacoes})

def depositar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
    if request.method == 'POST':
        form = OperacaoForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            conta.saldo += valor
            conta.save()
            Movimentacao.objects.create(conta=conta, tipo='D', valor=valor)
            messages.success(request, 'Depósito realizado com sucesso!')
            return redirect('detalhe_conta', conta_id=conta.id)
    else:
        form = OperacaoForm()
    return render(request, 'core/operacao.html', {'form': form, 'conta': conta, 'acao': 'Depósito'})

def sacar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
    if request.method == 'POST':
        form = OperacaoForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            if conta.saldo >= valor:
                conta.saldo -= valor
                conta.save()
                Movimentacao.objects.create(conta=conta, tipo='S', valor=valor)
                messages.success(request, 'Saque realizado com sucesso!')
                return redirect('detalhe_conta', conta_id=conta.id)
            else:
                messages.error(request, 'Saldo insuficiente.')
    else:
        form = OperacaoForm()
    return render(request, 'core/operacao.html', {'form': form, 'conta': conta, 'acao': 'Saque'})