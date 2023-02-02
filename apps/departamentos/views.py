from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)
        # try:
        #     self.departamento = self.request.user.departamento
        #     empresa_logada = self.departamento.empresa
        #     funcionarios = Departamento.objects.filter(empresa=empresa_logada)
        #     return funcionarios
        # except Departamento.DoesNotExist:
        #     return render(self.request, 'departamentos/departamento_does_not_exist.html', status=404)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome', 'empresa']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.departamento = obj
        funcionario.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome', 'empresa']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
