# Generated by Django 2.2 on 2019-04-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20190408_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='default_allotment',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
            preserve_default=False,
        ),
    ]
