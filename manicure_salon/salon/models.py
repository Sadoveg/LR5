from django.db import models


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=120)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')
    duration = models.CharField('Длительность', max_length=50)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField('Имя мастера', max_length=120)
    experience = models.CharField('Опыт работы', max_length=50)
    specialization = models.CharField('Специализация', max_length=150)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return self.name


class Appointment(models.Model):
    client_name = models.CharField('Имя клиента', max_length=120)
    phone = models.CharField('Телефон', max_length=30)
    service = models.CharField('Услуга', max_length=120)
    date = models.DateField('Дата записи')
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Запись клиента'
        verbose_name_plural = 'Записи клиентов'

    def __str__(self):
        return f'{self.client_name} — {self.service}'
