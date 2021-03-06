# Generated by Django 4.0.3 on 2022-04-06 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_age', models.PositiveIntegerField(verbose_name='Минимальный возраст')),
                ('max_age', models.PositiveIntegerField(verbose_name='Максимальный возраст')),
            ],
            options={
                'verbose_name_plural': 'Категории возрастов',
                'unique_together': {('min_age', 'max_age')},
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('trainings_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во тренировок')),
                ('trainings_freeze_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во заморозок')),
            ],
            options={
                'verbose_name_plural': 'Дети',
            },
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=128, verbose_name='Заголовок события в галерее')),
                ('description', models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание галереи')),
                ('galery_photo', models.ImageField(upload_to='', verbose_name='Фото галереи')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Галереи',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение новости')),
                ('description', models.TextField(max_length=4096, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('trainings_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во тренировок')),
                ('trainings_freeze_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во заморозок')),
            ],
            options={
                'verbose_name_plural': 'Пакеты тренировок',
                'unique_together': {('trainings_count', 'trainings_freeze_count')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='PreRegisterUserEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email с приглашением')),
            ],
            options={
                'verbose_name_plural': 'Предрегистрационные почтовые адреса',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.person', verbose_name='Личность')),
            ],
            options={
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='PhotoInGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_photo', models.ImageField(upload_to='', verbose_name='Изображение события')),
                ('galery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.galery', verbose_name='Галерея')),
            ],
            options={
                'verbose_name_plural': 'Фотографии в галерее',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.person', verbose_name='Личность')),
            ],
            options={
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название группы')),
                ('age_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.agecategory', verbose_name='Возрастная группа')),
                ('children', models.ManyToManyField(blank=True, to='mainapp.child', verbose_name='Дети группы')),
                ('trainers', models.ManyToManyField(blank=True, to='mainapp.trainer', verbose_name='Тренеры группы')),
            ],
            options={
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название отделения')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес отделения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение отделения')),
                ('groups', models.ManyToManyField(blank=True, to='mainapp.group', verbose_name='Группы отделения')),
                ('packs', models.ManyToManyField(blank=True, to='mainapp.pack', verbose_name='Пакеты отделения')),
                ('trainers', models.ManyToManyField(blank=True, to='mainapp.trainer', verbose_name='Тренеры отделения')),
            ],
            options={
                'verbose_name_plural': 'Отделения',
            },
        ),
        migrations.AddField(
            model_name='child',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.person', verbose_name='Личность'),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата тренировки')),
                ('starttime', models.TimeField(verbose_name='Начало')),
                ('endtime', models.TimeField(verbose_name='Конец')),
                ('status', models.CharField(choices=[('not_stated', 'Неопределенный'), ('done', 'Выполнена'), ('not_took_place', 'Не состоялась')], default='not_stated', max_length=14, verbose_name='Состояние')),
                ('children', models.ManyToManyField(blank=True, default=None, to='mainapp.child', verbose_name='Дети присутствовавшие на тренировке')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department', verbose_name='Отделение')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group', verbose_name='Группа')),
                ('reserve_trainers', models.ManyToManyField(blank=True, default=None, to='mainapp.trainer', verbose_name='Заменяющие тренеры')),
            ],
            options={
                'verbose_name_plural': 'Тренировки',
                'unique_together': {('date', 'department', 'group', 'starttime', 'endtime')},
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], verbose_name='День тренировки')),
                ('starttime', models.TimeField(verbose_name='Время начала тренировки')),
                ('endtime', models.TimeField(verbose_name='Время окончания тренировки')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department', verbose_name='Отделение')),
                ('groups', models.ManyToManyField(to='mainapp.group', verbose_name='Группы')),
            ],
            options={
                'verbose_name_plural': 'Расписание',
                'unique_together': {('train_day', 'department', 'starttime', 'endtime')},
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.child', verbose_name='Ребенок')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.pack', verbose_name='Пакет')),
            ],
            options={
                'verbose_name_plural': 'Платежи',
                'unique_together': {('timestamp', 'child', 'pack')},
            },
        ),
    ]
