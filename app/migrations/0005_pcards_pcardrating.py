# Generated by Django 5.0.2 on 2024-03-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pcards_pcardoldprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcards',
            name='pcardrating',
            field=models.IntegerField(default=5, max_length=10),
            preserve_default=False,
        ),
    ]
