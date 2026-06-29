from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas')
    numero_conta = models.CharField(max_length=10, unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Conta {self.numero_conta} - {self.cliente.nome}"

class Movimentacao(models.Model):
    TIPOS = (
        ('D', 'Depósito'),
        ('S', 'Saque'),
    )
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=1, choices=TIPOS)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor}"