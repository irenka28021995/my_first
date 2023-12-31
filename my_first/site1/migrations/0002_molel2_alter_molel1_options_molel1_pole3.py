# Generated by Django 4.1.7 on 2023-02-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Molel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pole1', models.IntegerField()),
                ('pole2', models.CharField(max_length=45)),
                ('pole3', models.TextField()),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.AlterModelOptions(
            name='molel1',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AddField(
            model_name='molel1',
            name='pole3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
