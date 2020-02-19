from django.db import models
from stdimage.models import StdImageField
# Create your models here.


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)


class Cardapio(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    bio = models.CharField('Bio', max_length=300)
    imagem = StdImageField('Imagem', upload_to='media', variations={'thumb': {'width': 480, 'height': 480}})

    class Meta:
        verbose_name = 'cardapio'
        verbose_name_plural = 'cardapios'

    def __str__(self):
        return self.nome
