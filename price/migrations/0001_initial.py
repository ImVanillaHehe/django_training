# Generated by Django 4.0.6 on 2022-08-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Цена')),
                ('pc_descriptions', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ценны',
                'verbose_name_plural': 'Ценны',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Описание')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Старая цена')),
                ('pt_new_price', models.CharField(max_length=200, verbose_name='Новая цена')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
