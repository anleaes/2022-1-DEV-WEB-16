from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SocialnetworkForm
from .models import Socialnetwork

# Create your views here.
def adiciona_projetos(request):
    template_name = 'projetos/adiciona_projetos.html'
    context = {}
    if request.method == 'POST':
        form = SocialnetworkForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('socialnetworks:lista_projetos')
    form = SocialnetworkForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_projetos(request):
    template_name = 'projetos/lista_projetos.html'
    socialnetworks = Socialnetwork.objects.filter()
    context = {
        'socialnetworks': socialnetworks
    }
    return render(request, template_name, context)

def edit_projetos(request, id_socialnetwork):
    template_name = 'projetos/adiciona_projetos.html'
    context ={}
    socialnetwork = get_object_or_404(Socialnetwork, id=id_socialnetwork)
    if request.method == 'POST':
        form = SocialnetworkForm(request.POST, instance=socialnetwork)
        if form.is_valid():
            form.save()
            return redirect('projetos:lista_projetos')
    form = SocialnetworkForm(instance=socialnetwork)
    context['form'] = form
    return render(request, template_name, context)

def delete_projetos(request, id_socialnetwork):
    socialnetwork = Socialnetwork.objects.get(id=id_socialnetwork)
    socialnetwork.delete()
    return redirect('projetos:lista_projetos')