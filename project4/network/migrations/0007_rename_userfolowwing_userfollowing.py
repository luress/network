# Generated by Django 3.2.8 on 2022-03-11 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_userfolowwing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFolowwing',
            new_name='UserFollowing',
        ),
    ]