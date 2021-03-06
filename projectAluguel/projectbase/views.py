from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from aluguel.forms import ImovelForm


def index(request):
    return render(request, 'projectbase/index.html')


def about(request):
    return render(request, 'projectbase/about.html')


def registrar_imovel(request):

    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)

        if form.is_valid():
            preview = form.save(commit=False)
            raw_slug_value = str(preview.numero) + '_' + preview.rua + '_' + preview.cep
            preview.slug = slugify(raw_slug_value)
            preview.save()
            return HttpResponseRedirect(reverse('projectbase:sucesso_registro'))
    else:
        form = ImovelForm()

    return render(request, 'projectbase/registrar.html', {'form': form})


def sucesso_registro(request):
    return render(request, 'projectbase/registroSucesso.html')
