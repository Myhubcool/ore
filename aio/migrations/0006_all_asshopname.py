# Generated by Django 2.1.3 on 2019-02-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aio', '0005_remove_all_asphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='asshopname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
