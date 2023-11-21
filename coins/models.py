from django.db import models
from django.urls import reverse

class Algo(models.Model):
    '''Алгоритмы'''
    title = models.CharField('Название алгоритма', max_length=50)
    description = models.TextField('Описание алгоритма', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Алгоритм'
        verbose_name_plural = 'Алгоритмы'

class Method(models.Model):
    '''Метод добычи'''
    title = models.CharField('Название метода', max_length=20)
    description = models.TextField('Описание метода', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Доказательство работы/доли'
        verbose_name_plural = 'Доказательство работы/доли'

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
    method = models.ManyToManyField(Method, blank=True, verbose_name='Доказательство работы/доли')
    algo = models.ManyToManyField(Algo, blank=True, verbose_name='Алгоритмы')
    currency = models.ManyToManyField(Currency, blank=True, verbose_name='Биржи')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}, {self.date_publ}'

    def get_absolute_url(self):
        return reverse('coin_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'

class Reviews(models.Model):
    '''Отзывы'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text = models.TextField('Текст отзыва', max_length=2000)
    coin = models.ForeignKey(Coin, verbose_name='Монета', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.coin}'

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
