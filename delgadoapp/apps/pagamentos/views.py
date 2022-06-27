from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PagamentoForm
from .models import Pagamento

# Create your views here.
@login_required(login_url='/contas/login/')
def add_pagamento(request):
    template_name = 'pagamentos/add_pagamentos.html'
    context = {}
    if request.method == 'POST':
        form = PagamentoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pagamentos:list_pagamentos')
    form = PagamentoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_pagamentos(request):
    template_name = 'pagamentos/list_pagamentos.html'
    pagamentos = Pagamento.objects.filter()
    context = {
        'pagamentos': pagamentos
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_pagamento(request, id_pagamento):
    template_name = 'pagamentos/add_pagamento.html'
    context ={}
    pagamento = get_object_or_404(Pagamento, id=id_pagamento)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, request.FILES,  instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamentos:list_pagamentos')
    form = PagamentoForm(instance=pagamento)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_pagamento(request, id_pagamento):
    pagamento = Pagamento.objects.get(id=id_pagamento)
    pagamento.delete()
    return redirect('pagamentos:list_pagamentos')