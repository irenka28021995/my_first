# Generated by Django 4.1.7 on 2023-02-27 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0004_remove_molel2_pole3'),
    ]

    operations = [
        migrations.AddField(
            model_name='molel2',
            name='pole3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='site1.molel1'),
            preserve_default=False,
        ),
    ]
