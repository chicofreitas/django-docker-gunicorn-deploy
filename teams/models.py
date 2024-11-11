from django.db import models

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _("Nome do Plano"),
        max_length=100,
        db_comment="Nome do plano de contas de propostas/projetos.",
    )
    description = models.CharField(
        _("Descrição"),
        max_length=200,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="Data de registo da proposta no sistema.",
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        db_comment="Data da última atualização realizada no resgistro da proposta (Projeto)",
    )
    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.name
