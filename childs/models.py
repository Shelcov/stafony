from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name='Название группы')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Child(models.Model):
    GENDER_CHOICES = (
        (1, 'Мужской'),
        (2, 'Женский')
    )
    photo = models.ImageField(upload_to='childs/', blank=True, null=True, default=None)
    name = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name='ФИО')
    gender = models.SmallIntegerField(default=1, choices=GENDER_CHOICES, verbose_name='Пол')
    birthdate = models.DateField(verbose_name='Дата рождения')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    is_studying = models.BooleanField(default=True, verbose_name='Обучается')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Ребёнок'
        verbose_name_plural = 'Дети'


class Log(models.Model):
    EVENT_CHOICES = (
        ('came', 'Пришёл'),
        ('away', 'Ушёл')
    )
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name='Ребёнок')
    event_time = models.DateTimeField(verbose_name='Привели/Забрали', auto_now_add=True)
    parent = models.TextField(verbose_name='Родитель')
    event_type = models.CharField(max_length=4, default='came', choices=EVENT_CHOICES, verbose_name='Тип')

    def __str__(self):
        return "%s %s в %s" % (self.child.name, self.event_type, self.event_time)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
