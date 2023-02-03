from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Documentos


class DocumentoCreate(CreateView):
    model = Documentos
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.documentos = obj
        self.object = obj
        funcionario.save()
        return super(DocumentoCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context




