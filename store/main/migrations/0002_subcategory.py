# Generated by Django 3.1.7 on 2021-03-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, verbose_name='Name')),
                ('category', models.ManyToManyField(to='main.Category')),
            ],
        ),
    ]