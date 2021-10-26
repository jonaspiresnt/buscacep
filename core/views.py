from django.shortcuts import Http404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from .forms import CepForm
from .get_endereco import get_endereco



class Index(FormView):
    template_name = 'core/index.html'
    form_class = CepForm


@csrf_exempt
def ajax_pesquisar_endereco(request):
    if request.is_ajax():
        data = dict()
        if request.method == 'POST':
            consulta = request.POST.get('consulta')
            resp = get_endereco(consulta)
            data['resposta'] = render_to_string('core/modal_resposta_cep.html', {'resp': resp}, request=request)
        else:
            data['html_form'] = render_to_string('core/modal_consulta_cep.html', request=request)
        return JsonResponse(data)
    else:
        raise Http404

