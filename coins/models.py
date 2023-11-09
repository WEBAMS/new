from django.db import models

class Algo(models.Model):
    '''Алгоритмы'''
    title = models.CharField('Название алгоритма', max_length=50)
    description = models.TextField('Описание алгоритма', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Алгоритм'
        verbose_name_plural = 'Алгоритмы'


class Currency (models.Model):
    '''Биржи'''
    title = models.CharField('Название биржи', max_length=50)
    description = models.TextField('Описание биржи', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Биржа'
        verbose_name_plural = 'Биржи'

class Coin(models.Model):
    '''Информация о монете'''
    title = models.CharField('Название монеты', max_length=100)
    imag = models.ImageField('Картинка', upload_to='image/&Y')
    description = models.TextField('Описание', blank=True)
    date_publ = models.DateField('Дата выхода')
    algo = models.ManyToManyField(Algo, verbose_name='Алгоритмы')
    currency = models.ManyToManyField(Currency, verbose_name='Биржи')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}, {self.date_publ}'

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
