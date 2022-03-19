# Generated by Django 3.2.8 on 2022-03-14 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_alter_userfollowing_following_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('liked_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post', to='network.post')),
                ('user_who_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]