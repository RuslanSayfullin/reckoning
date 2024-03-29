# Generated by Django 4.1.5 on 2023-01-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reckoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, editable=False, max_length=40, unique=True)),
                ('designer', models.CharField(max_length=100, verbose_name='Дизайнер')),
                ('client_data', models.CharField(max_length=100, verbose_name='Данные клиента')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон Клиента')),
                ('date', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
