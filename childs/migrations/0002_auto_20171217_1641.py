# Generated by Django 2.0 on 2017-12-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.RemoveField(
            model_name='log',
            name='created',
        ),
        migrations.AlterField(
            model_name='log',
            name='event_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Привели/Забрали'),
        ),
    ]
