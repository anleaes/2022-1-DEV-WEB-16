from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GeneroForm
from .models import Genero

def adiciona_generos(request):
    template_name = 'generos/adiciona_generos.html'
    context = {}
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('generos:lista_generos')
    form = GeneroForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_generos(request):
    template_name = 'generos/lista_generos.html'
    generos = Genero.objects.filter()
    context = {
        'generos': generos
    }
    return render(request, template_name, context)

def edit_generos(request, id_genero):
    template_name = 'generos/adiciona_generos.html'
    context ={}
    generos = get_object_or_404(Genero, id=id_genero)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=generos)
        if form.is_valid():
            form.save()
            return redirect('generos:lista_generos')
    form = GeneroForm(instance=generos)
    context['form'] = form
    return render(request, template_name, context)

def delete_generos(request, id_genero):
    genero = Genero.objects.get(id=id_genero)
    genero.delete()
    return redirect('generos:lista_generos')