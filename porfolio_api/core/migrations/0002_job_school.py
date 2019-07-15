# Generated by Django 2.2.3 on 2019-07-15 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('degree', models.CharField(max_length=35)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('url', models.URLField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='core.Bio')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=35)),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=80)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='core.Bio')),
            ],
        ),
    ]
