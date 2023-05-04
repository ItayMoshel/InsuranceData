# Generated by Django 4.1.4 on 2023-05-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('bmi', models.FloatField()),
                ('children', models.IntegerField()),
                ('smoker', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=20)),
                ('predicted_price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]