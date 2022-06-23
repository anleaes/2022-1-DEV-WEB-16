from typing import Tuple
from django.db import models
from socialnetworks.models import Socialnetwork

# Create your models here.
class Client(models.Model):
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

    gender = models.ForeignKey( Socialnetwork, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name

class ClientSocialnetwork(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(Socialnetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Redes Social'
        verbose_name_plural = 'Itens de Rede Social'
        ordering =['id']

    def __str__(self):
        return self.socialnetwork.name