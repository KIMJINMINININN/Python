# Generated by Django 3.0 on 2019-12-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('date', models.TextField()),
                ('content', models.TextField(default='', null=True)),
            ],
        ),
    ]
