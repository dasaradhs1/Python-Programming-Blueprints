# Generated by Django 2.0.1 on 2018-02-15 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180215_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-highlighted', 'name']},
        ),
        migrations.RenameField(
            model_name='game',
            old_name='promoted',
            new_name='highlighted',
        ),
    ]
