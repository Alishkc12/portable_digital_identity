# Generated by Django 3.2.6 on 2021-11-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept_list',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
