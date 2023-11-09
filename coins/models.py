from django.db import models

class Coin(models.Model):
    '''Информация о монете'''
    title = models.CharField('Название монеты', max_length=100)
    imag = models.ImageField('Картинка', upload_to='image/&Y')
    description = models.TextField('Описание', blank=True)
    date_publ = models.DateField('Дата выхода')

    def __str__(self):
        return f'{self.title}, {self.date_publ}'

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
