# Generated by Django 5.0.2 on 2024-03-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pcards_pcarddiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcards',
            name='pcardoldprice',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
