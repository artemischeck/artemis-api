# Generated by Django 2.2.11 on 2020-04-09 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'UP'), (2, 'WARN'), (3, 'SLOW'), (4, 'DOWN'), (5, 'OFF')])),
                ('delay', models.IntegerField(default=600, help_text='Time delay in seconds before sending the next alert message')),
                ('channels', models.CharField(help_text='Channels list i.e comma separated', max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts_settings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
