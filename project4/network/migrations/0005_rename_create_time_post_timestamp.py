# Generated by Django 3.2.8 on 2022-03-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='timestamp',
        ),
    ]