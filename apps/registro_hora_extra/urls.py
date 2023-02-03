from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_registro_hora_extra'),
]
