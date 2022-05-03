# Generated by Django 4.0.4 on 2022-05-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_historicaluser_username_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='marital_status',
            field=models.CharField(max_length=50, null=True, verbose_name='Estado civil'),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='user',
            name='marital_status',
            field=models.CharField(max_length=50, null=True, verbose_name='Estado civil'),
        ),
    ]
