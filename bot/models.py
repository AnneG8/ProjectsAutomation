from django.db import models


class Project(models.Model):
    title = models.CharField('Название', max_length=50)
    start_day = models.DateField('День начала проекта')
    #стадия проекта: объявлен, сообщения разосланны, уточнения разосланы, команды сформированы, запущен, закончен
    #teams

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField('Название', max_length=100)
    project = models.ForeignKey(
        Project,
        verbose_name='Проект',
        on_delete=models.SET_NULL,
        related_name='teams',
        null=True
    )
    pm = models.ForeignKey(
        'ProjectManager',
        verbose_name='Руководитель проекта',
        on_delete=models.SET_NULL,
        related_name='curr_teams',
        null=True,
        blank=True
    )
    #students
    call_start = models.TimeField(
        'Начало созвона',
        null=True,
        blank=True
    )
    is_approved = models.BooleanField(
        'Утверждена',
        default=False
    )
    #Ссылка на бриф

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.title


class Member(models.Model):
    id_telegram = models.CharField('Телеграм id', max_length=20)
    name = models.CharField('Имя', max_length=30)
    nickname = models.CharField('Ник в телеграме', max_length=30, null=True)
    time_from = models.TimeField('Время от', null=True, blank=True)
    time_to = models.TimeField('Время до', null=True, blank=True)
    good_partners = models.ManyToManyField(
        'self',
        verbose_name='Рекомендуемые напарники',
        symmetrical=True,
        blank=True
    )
    bad_partners = models.ManyToManyField(
        'self',
        verbose_name='Нерекомендуемые напарники',
        symmetrical=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.name


class StudyLevel(models.Model):
    level = models.CharField('Уровень', max_length=20, unique=True)
    #students

    class Meta:
        verbose_name = 'Уровень обучения'
        verbose_name_plural = 'Уровни обучения'

    def __str__(self):
        return self.level


class Student(Member):
    level = curr_team = models.ForeignKey(
        StudyLevel,
        verbose_name='Уровень',
        on_delete=models.PROTECT,
        related_name='students',
        default=1
    )
    curr_team = models.ForeignKey(
        Team,
        verbose_name='Текущая команда',
        on_delete=models.SET_NULL,
        related_name='students',
        null=True,
        blank=True
    )
    #teams - все команды, в которых был

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class ProjectManager(Member):
    #curr_teams

    class Meta:
        verbose_name = 'Руководитель проектов'
        verbose_name_plural = 'Руководители проектов'

    def __str__(self):
        return self.name

