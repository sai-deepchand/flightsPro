# Generated by Django 3.0.4 on 2020-03-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200322_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='xyz', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='xyz', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(default='xyz', max_length=30),
        ),
    ]
