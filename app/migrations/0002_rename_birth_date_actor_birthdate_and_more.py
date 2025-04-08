# Generated by Django 5.2 on 2025-04-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='birth_date',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='app.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(),
        ),
    ]
