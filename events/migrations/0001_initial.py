# Generated by Django 3.0.5 on 2020-04-08 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=140)),
                ('status', models.BooleanField(default=False)),
                ('host', models.CharField(max_length=140)),
                ('tags', models.CharField(max_length=400)),
                ('details', models.TextField(blank=True, null=True)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=11)),
                ('datetime', models.DateField()),
                ('incident', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolved', models.BooleanField(default=False)),
                ('threshold', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='events.Events')),
            ],
        ),
    ]
