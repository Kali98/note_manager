# Generated by Django 3.1.2 on 2020-10-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_api', '0005_auto_20201002_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notechange',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
