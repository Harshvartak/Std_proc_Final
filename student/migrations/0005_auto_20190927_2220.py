# Generated by Django 2.2.5 on 2019-09-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190927_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]