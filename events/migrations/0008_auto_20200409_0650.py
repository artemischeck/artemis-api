# Generated by Django 2.2.11 on 2020-04-09 06:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_auto_20200409_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='service',
            new_name='label',
        ),
        migrations.AlterUniqueTogether(
            name='services',
            unique_together={('label', 'host', 'owner')},
        ),
    ]
