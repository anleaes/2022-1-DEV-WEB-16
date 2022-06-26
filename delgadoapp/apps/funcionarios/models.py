from typing import Tuple
from django.db import models
from projetos.models import Projeto
from orders.models import OrderItem

# Create your models here.
class Funcionario(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    # last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)

    JOB_CHOICES = (
        ('TL', 'Tech Lead'),
        ('PM', 'Product Manager'),
        ('ES', 'Engenheiro de Software'),
    )
    job = models.CharField('Profissao', max_length=2, choices=JOB_CHOICES)
    DEPARTAMENT_CHOICES = (
        ('PEX', 'Investment Plataform'),
        ('BRK', 'Broker'),
        ('OB', 'Onboarding'),
        ('TR', 'Trade'),
    )
    departament = models.CharField('Departamento', max_length=3, choices=DEPARTAMENT_CHOICES)

    gender = models.ForeignKey( Projeto, on_delete=models.CASCADE)
    project = models.ManyToManyField(OrderItem, through='FuncionarioProject', blank=True)
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering =['id']

    def __str__(self):
        return self.first_name

class FuncionarioProjeto(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Redes Social'
        verbose_name_plural = 'Itens de Rede Social'
        ordering =['id']

    def __str__(self):
        return self.projeto.name


class FuncionarioProject(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    project = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionário do projeto'
        verbose_name_plural = 'Funcionários dos projetos'
        ordering =['id']

    def __str__(self):
        return self.project.name