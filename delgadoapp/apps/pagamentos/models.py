from django.db import models
from funcionarios.models import Funcionario

# Create your models here.
class Pagamento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # name = models.CharField('Nome', max_length=50)
    funcionario = models.ForeignKey( Funcionario, on_delete=models.CASCADE)
    # description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    # photo = models.ImageField('Foto', upload_to='photos')
    # doc = models.FileField('Documentos', upload_to='docs')

    JOB_CHOICES = (
        ('TL', 'Tech Lead'),
        ('PM', 'Product Manager'),
        ('ES', 'Engenheiro de Software'),
    )
    job = models.CharField('Profissao', max_length=2, choices=JOB_CHOICES)
    salary = models.BigIntegerField('Salario')

    DEPARTAMENT_CHOICES = (
        ('PEX', 'Investment Plataform'),
        ('BRK', 'Broker'),
        ('OB', 'Onboarding'),
        ('TR', 'Trade'),
    )
    departament = models.CharField('Departamento', max_length=3, choices=DEPARTAMENT_CHOICES)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return self.name

class PagamentoFuncionario(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pagamento do funcionario'
        verbose_name_plural = 'Pagamentos dos funcionarios'
        ordering =['id']

    def __str__(self):
        return self.funcionario.name