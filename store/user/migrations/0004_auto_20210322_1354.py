# Generated by Django 3.1.7 on 2021-03-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_typeuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='typeUser',
            field=models.CharField(choices=[('E', 'Employee'), ('C', 'Client'), ('D', 'DEV'), ('A', 'Admin')], max_length=9, null='C', verbose_name='Type User'),
        ),
    ]