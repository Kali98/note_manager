# Generated by Django 3.1.2 on 2020-10-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_api', '0002_notechange'),
    ]

    operations = [
        migrations.AddField(
            model_name='notechange',
            name='action',
            field=models.CharField(default='Updated', max_length=10),
            preserve_default=False,
        ),
    ]
