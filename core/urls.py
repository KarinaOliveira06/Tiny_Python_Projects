from django.urls import path
from . import views

urlpatterns = [
    path('conta/<int:conta_id>/', views.detalhe_conta, name='detalhe_conta'), # Exibe Saldo e Histórico
    path('conta/<int:conta_id>/depositar/', views.depositar, name='depositar'),
    path('conta/<int:conta_id>/sacar/', views.sacar, name='sacar'),
]