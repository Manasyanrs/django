# Generated by Django 5.0.1 on 2024-02-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_rename_auth_user_profile_user_remove_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'user data', 'verbose_name_plural': 'additional user data'},
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(default='', max_length=25, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(db_index=True, default='', max_length=25, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='verification_flag',
            field=models.BooleanField(default=False, verbose_name='verification_flag'),
        ),
    ]