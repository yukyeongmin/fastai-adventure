# Generated by Django 2.2.17 on 2021-02-08 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20210208_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='create_data',
            new_name='create_date',
        ),
    ]