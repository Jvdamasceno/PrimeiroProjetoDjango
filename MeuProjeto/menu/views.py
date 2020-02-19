from django.contrib import messages
from django.views.generic import FormView, TemplateView
from .models import Cardapio
from .forms import ContatoForm
from django.urls import reverse_lazy
# Create your views here.


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs, ):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cardapio'] = Cardapio.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_mail()
        messages.error(self.request, 'Error ao envir Email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class PratosView(TemplateView):
    template_name = 'pratos.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PratosView, self).get_context_data(**kwargs)
        context['pratos'] = Cardapio.objects.get(id=self.kwargs['pk'])
        return context

