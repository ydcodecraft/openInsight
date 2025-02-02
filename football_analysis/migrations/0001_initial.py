# Generated by Django 5.1 on 2024-08-21 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('age', models.IntegerField(default=0)),
                ('height', models.FloatField(default=0)),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='football_analysis.club')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Date When the Match Took Place')),
                ('home_team_score', models.IntegerField(default=0)),
                ('away_team_score', models.IntegerField(default=0)),
                ('away_team', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='away_team', to='football_analysis.club')),
                ('home_team', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='football_analysis.club')),
                ('stadium', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='football_analysis.stadium')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='home_stadium',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='football_analysis.stadium'),
        ),
    ]
