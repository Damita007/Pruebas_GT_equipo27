# Generated by Django 4.0.4 on 2022-05-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_historicaluser_age_historicaluser_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='email_alternative',
            field=models.EmailField(max_length=255, null=True, verbose_name='Correo Electrónico alternativo'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='residence',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Residencia actual'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_alternative',
            field=models.EmailField(max_length=255, null=True, verbose_name='Correo Electrónico alternativo'),
        ),
        migrations.AddField(
            model_name='user',
            name='residence',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Residencia actual'),
        ),
    ]
