from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    """
        Nome e email são as informações mínimas
         para alguém se inscrever em um evento.
    """
    nome = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    cpf = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

    def inscrever_em_evento(self, evento, tipo):
        evento.realizar_inscricao(evento, self, tipo)

    class Meta:
        verbose_name_plural = 'Usuários'


class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    organizador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="meus_eventos")

    def __str__(self):
        return self.nome
    
    def add_inscricao(self, tipo_evento, usuario_inscrito):
        """Inscrever um usuário no Evento e retornar a Inscricao"""
        nova_inscricao = Inscricao.objects.create(
            evento=self, tipo=tipo_evento, inscrito=usuario_inscrito)
        return nova_inscricao

    def add_tipo_inscricao(self, nome, descricao, preco, quantidade, data_inicio_vendas, data_fim_vendas):
        """Adiciona um tipo de Inscrição ao evento. Exemplo: Gratuita."""
        novo_tipo_inscricao = TipoInscricao.objects.create(
            evento=self, nome=nome,
            descricao=descricao, preco=preco,
            quantidade=quantidade,
            data_inicio_vendas=data_inicio_vendas,
            data_fim_vendas=data_fim_vendas
        )
        return novo_tipo_inscricao
    
    class Meta:
        verbose_name_plural = 'Eventos'


class TipoInscricao(models.Model):
    """
    Quanto custa, qual período, o que está embutido no preço?
    """
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    quantidade = models.IntegerField()
    data_inicio_vendas = models.DateTimeField()
    data_fim_vendas = models.DateTimeField()

    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='evento')

    def __str__(self):
        return f'{self.nome} - {self.preco}'

    class Meta:
        verbose_name_plural = 'Tipos de Inscrições'


class Inscricao(models.Model):
    data = models.DateTimeField(auto_now_add=True)

    tipo = models.ForeignKey(
        TipoInscricao,
        on_delete=models.DO_NOTHING)

    evento = models.ForeignKey(
        Evento,
        on_delete=models.DO_NOTHING)

    inscrito = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        related_name='minhas_inscricoes')

    def __str__(self):
        return self.data

    class Meta:
        verbose_name_plural = 'Inscrições'

