from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView)
from django.shortcuts import render
from .models import Funcionario


@method_decorator(login_required, name='dispatch')
class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        try:
            self.funcionario = self.request.user.funcionario
            empresa_logada = self.funcionario.empresa
            funcionarios = Funcionario.objects.filter(empresa=empresa_logada)
            return funcionarios
        except Funcionario.DoesNotExist:
            return render(self.request, 'funcionarios/funcionario_does_not_exist.html', status=404)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
