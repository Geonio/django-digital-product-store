# Generated by Django 2.1.11 on 2020-07-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.TextField(max_length=150, verbose_name='Описание товара')),
                ('icon', models.ImageField(upload_to='icon', verbose_name='Иконка товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('count', models.IntegerField()),
                ('unique_id', models.CharField(default='tIqRKpDgkpLHLODHdyWbnzQjoAHGfoRAkXpHFxLH', max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-id'],
            },
        ),
    ]
