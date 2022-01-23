# Generated by Django 3.2.11 on 2022-01-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20220122_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='slug',
        ),
        migrations.AddField(
            model_name='course',
            name='update_time',
            field=models.DateTimeField(auto_now=True, help_text='该条记录的更新时间', verbose_name='更新时间'),
        ),
    ]
