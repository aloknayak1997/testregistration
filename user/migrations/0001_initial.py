# Generated by Django 2.0.5 on 2018-08-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('mob_no', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
