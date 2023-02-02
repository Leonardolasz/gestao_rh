from django.urls import path
from .views import DepartamentoList, DepartamentoCreate, DepartamentoEdit, DepartamentoDelete


urlpatterns = [
    path('listar/', DepartamentoList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoEdit.as_view(), name='update_departamento'),
    path('apagar/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),

]
