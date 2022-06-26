from ast import Or
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm
from .models import Projeto

def list_projetos(request):
    template_name = 'projetos/list_projetos.html'
    projetos = Projeto.objects.filter()
    context = {
        'projetos': projetos,
    }
    return render(request, template_name, context)

def add_projeto(request):
    template_name = 'projetos/add_projeto.html'
    context = {}
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('projetos:list_projetos')
    form = ProjetoForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    projeto.delete()
    return redirect('projetos:list_projetos')

def edit_projeto(request, id_projeto):
    template_name = 'projetos/add_projeto.html'
    context ={}
    projeto = get_object_or_404(Projeto, id=id_projeto)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos:list_projetos')
    form = ProjetoForm(instance=projeto)
    context['form'] = form
    return render(request, template_name, context)