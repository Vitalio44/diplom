# Generated by Django 2.2.16 on 2020-09-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200909_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
    ]