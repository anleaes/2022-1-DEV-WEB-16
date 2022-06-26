from django.shortcuts import render, get_object_or_404, redirect
from .forms import FuncionarioForm
from .models import Projeto, FuncionarioProjeto, Funcionario

# Create your views here.
def add_funcionario(request):
    template_name = 'funcionarios/add_funcionario.html'
    context = {}
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('funcionarios:list_funcionarios')
    form = FuncionarioForm()
    context['form'] = form
    return render(request, template_name, context)

def list_funcionarios(request):
    template_name = 'funcionarios/list_funcionarios.html'
    funcionario_projeto = FuncionarioProjeto.objects.filter()
    projetos = Projeto.objects.filter()
    funcionarios = Funcionario.objects.filter()
    context = {
        'funcionarios': funcionarios,
        'projetos': projetos,
        'funcionario_projetos': funcionario_projeto
    }
    return render(request, template_name, context)

def edit_funcionario(request, id_funcionario):
    template_name = 'funcionarios/add_funcionario.html'
    context ={}
    funcionario = get_object_or_404(Funcionario, id=id_funcionario)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:list_funcionarios')
    form = FuncionarioForm(instance=funcionario)
    context['form'] = form
    return render(request, template_name, context)

def delete_funcionario(request, id_funcionario):
    funcionario = Funcionario.objects.get(id=id_funcionario)
    funcionario.delete()
    return redirect('funcionarios:list_funcionarios')

def search_funcionarios(request):
    template_name = 'funcionarios/list_funcionarios.html'
    query = request.GET.get('query')
    funcionario_projetos = FuncionarioProjeto.objects.filter()
    projetos = Projeto.objects.filter()
    funcionarios = Funcionario.objects.filter(last_name__icontains=query)
    context = {
        'funcionarios': funcionarios,
        'projetos': projetos,
        'funcionario_projetos': funcionario_projetos
    }
    return render(request,template_name, context)