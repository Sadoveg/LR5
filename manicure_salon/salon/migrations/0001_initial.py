# Generated manually for laboratory work

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=120, verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('service', models.CharField(max_length=120, verbose_name='Услуга')),
                ('date', models.DateField(verbose_name='Дата записи')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Запись клиента',
                'verbose_name_plural': 'Записи клиентов',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя мастера')),
                ('experience', models.CharField(max_length=50, verbose_name='Опыт работы')),
                ('specialization', models.CharField(max_length=150, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('duration', models.CharField(max_length=50, verbose_name='Длительность')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
