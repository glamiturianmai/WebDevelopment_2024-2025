from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратные связи'
        ordering = ['-created_at']

    def __str__(self):
        return f'Сообщение от {self.name}'