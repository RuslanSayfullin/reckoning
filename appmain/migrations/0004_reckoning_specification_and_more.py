# Generated by Django 4.1.5 on 2023-02-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0003_alter_reckoning_designer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reckoning',
            name='specification',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='reckoning',
            name='total_discounted_price',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='reckoning',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
