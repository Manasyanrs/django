# Generated by Django 4.1 on 2022-09-07 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, default='', max_length=120, verbose_name='название')),
                ('body', models.TextField(blank=True, default='', verbose_name='содержание')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('update_date', models.DateField(auto_now=True, verbose_name='дата редактирования')),
                ('flag_activate', models.BooleanField(default=True, verbose_name='флаг активности')),
                ('status', models.CharField(choices=[('on', 'actively'), ('off', 'not active')], default='off', max_length=3, verbose_name='Статус активности')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'db_table': 'News',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('count_of_employers', models.IntegerField()),
                ('director', models.CharField(max_length=30)),
                ('chef', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('house', models.IntegerField()),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
                ('serves_sushi', models.BooleanField(default=False)),
                ('serves_burgers', models.BooleanField(default=False)),
                ('serves_donats', models.BooleanField(default=False)),
                ('serves_coffee', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Ресторан',
                'db_table': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('house', models.IntegerField()),
                ('apartment', models.IntegerField()),
                ('seniority', models.TextField()),
                ('education', models.TextField(max_length=50)),
                ('cources', models.TextField(max_length=50)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'verbose_name': 'Официант',
                'verbose_name_plural': 'Официант',
                'db_table': 'Waiter',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, default='', max_length=16, verbose_name='имя пользователя')),
                ('text', models.CharField(default='', max_length=1024, verbose_name='текст комментария')),
                ('status', models.CharField(choices=[('y', 'Удалено администратором')], default=None, max_length=1, verbose_name='Удалено администратором')),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='restaurants.news', verbose_name='связь с моделью новость')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='app_users.user', verbose_name='связь с моделью пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий',
                'db_table': 'Comments',
            },
        ),
    ]
