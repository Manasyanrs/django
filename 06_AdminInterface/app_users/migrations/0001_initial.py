# Generated by Django 4.1 on 2022-09-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, default='', max_length=25, verbose_name='имя пользователя')),
                ('password', models.CharField(default='', max_length=25, verbose_name='пароль пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
                'db_table': 'User',
            },
        ),
    ]