# Generated by Django 3.0.3 on 2020-03-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_game_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='game_id',
            field=models.IntegerField(default=0),
        ),
    ]