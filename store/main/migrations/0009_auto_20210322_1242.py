# Generated by Django 3.1.7 on 2021-03-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210322_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='subCategory',
        ),
        migrations.AddField(
            model_name='item',
            name='subCategory',
            field=models.ManyToManyField(null=True, to='main.SubCategory'),
        ),
    ]