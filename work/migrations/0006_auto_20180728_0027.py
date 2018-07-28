# Generated by Django 2.0.7 on 2018-07-28 00:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20180727_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='level2',
            name='level1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Level1'),
        ),
        migrations.AddField(
            model_name='level3',
            name='level2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Level2'),
        ),
        migrations.AlterField(
            model_name='task',
            name='day',
            field=models.DateField(default=datetime.date(2018, 7, 28)),
        ),
    ]
