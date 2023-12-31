# Generated by Django 4.1.7 on 2023-03-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0007_molel3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Molel4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pole1', models.CharField(max_length=45, verbose_name='Название')),
                ('pole2', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.AlterField(
            model_name='molel3',
            name='pole1',
            field=models.CharField(max_length=45, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='molel3',
            name='pole2',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
