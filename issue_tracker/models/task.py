from django.core.validators import MinLengthValidator
from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=200,
        verbose_name="Краткое описание",
        validators=(MinLengthValidator(limit_value=3),)
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name="Полное описание"
    )
    status = models.ForeignKey(
        'issue_tracker.Status',
        on_delete=models.PROTECT
    )
    types = models.ManyToManyField(
        to='issue_tracker.Type',
        related_name='tasks',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    project = models.ForeignKey(
        'issue_tracker.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Проект',
        default=1,
    )

    def __str__(self):
        return self.summary
