# Generated by Django 3.1.7 on 2021-03-30 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blue', models.CharField(max_length=50)),
                ('red', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.CharField(max_length=5)),
                ('content', models.CharField(max_length=50)),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='either.vote')),
            ],
        ),
    ]
