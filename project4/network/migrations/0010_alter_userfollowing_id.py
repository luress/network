# Generated by Django 3.2.8 on 2022-03-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
