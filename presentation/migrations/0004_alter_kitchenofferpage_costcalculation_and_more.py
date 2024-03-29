# Generated by Django 4.1.5 on 2023-02-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_kitchenofferpage_total_discounted_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchenofferpage',
            name='costcalculation',
            field=models.FileField(blank=True, null=True, upload_to='costcalculation/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='kitchenofferpage',
            name='sketch',
            field=models.ImageField(blank=True, null=True, upload_to='sketch/%Y/%m/%d/', verbose_name='Эскиз'),
        ),
    ]
