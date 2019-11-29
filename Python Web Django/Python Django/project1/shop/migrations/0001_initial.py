# Generated by Django 2.2.5 on 2019-11-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itm_no', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(max_length=100)),
                ('itm_content', models.TextField()),
                ('itm_price', models.IntegerField()),
                ('itm_qty', models.IntegerField()),
                ('itm_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
