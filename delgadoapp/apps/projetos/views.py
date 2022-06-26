from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm
from .models import Projeto

def adiciona_projetos(request):
    template_name = 'projetos/adiciona_projetos.html'
    context = {}
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('projetos:lista_projetos')
    form = ProjetoForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_projetos(request):
    template_name = 'projetos/lista_projetos.html'
    projetos = Projeto.objects.filter()
    context = {
        'projetos': projetos
    }
    return render(request, template_name, context)

def edit_projetos(request, id_projeto):
    template_name = 'projetos/adiciona_projetos.html'
    context ={}
    projetos = get_object_or_404(Projeto, id=id_projeto)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projetos)
        if form.is_valid():
            form.save()
            return redirect('projetos:lista_projetos')
    form = ProjetoForm(instance=projetos)
    context['form'] = form
    return render(request, template_name, context)

def delete_projetos(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    projeto.delete()
    return redirect('projetos:lista_projetos')