# Generated by Django 5.0.2 on 2024-03-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcards',
            name='pcardimg',
            field=models.FileField(default=None, null=True, upload_to='app/'),
        ),
    ]