# Generated by Django 3.2.2 on 2021-05-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210511_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_order',
            name='cost',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6, max_length=20),
        ),
        migrations.AlterField(
            model_name='new_order',
            name='id',
            field=models.CharField(default='HF67EB124C', max_length=15, primary_key=True, serialize=False),
        ),
    ]