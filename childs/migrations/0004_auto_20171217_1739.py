# Generated by Django 2.0 on 2017-12-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childs', '0003_auto_20171217_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='childs/'),
        ),
    ]
