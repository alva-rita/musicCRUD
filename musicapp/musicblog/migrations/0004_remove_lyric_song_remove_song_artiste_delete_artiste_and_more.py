# Generated by Django 4.1.3 on 2022-11-06 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicblog', '0003_alter_song_artiste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='Song',
        ),
        migrations.RemoveField(
            model_name='song',
            name='Artiste',
        ),
        migrations.DeleteModel(
            name='Artiste',
        ),
        migrations.DeleteModel(
            name='Lyric',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
