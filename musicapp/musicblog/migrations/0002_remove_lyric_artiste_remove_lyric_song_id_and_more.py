# Generated by Django 4.1.2 on 2022-10-29 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='Artiste',
        ),
        migrations.RemoveField(
            model_name='lyric',
            name='song_id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artiste_id',
        ),
        migrations.AddField(
            model_name='lyric',
            name='Song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicblog.song'),
        ),
        migrations.AlterField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(),
        ),
    ]
