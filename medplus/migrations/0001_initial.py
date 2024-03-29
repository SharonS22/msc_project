# Generated by Django 2.1.5 on 2022-07-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('outbreak', models.CharField(max_length=100)),
                ('full_loc', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=50)),
                ('continent', models.CharField(max_length=100)),
                ('updates', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'datas',
            },
        ),
    ]
