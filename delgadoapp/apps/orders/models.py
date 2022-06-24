from django.db import models

class OrderItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField('Descricao', max_length=300)
    project = models.CharField('Projeto', max_length=50)

    class Meta:
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.project) 