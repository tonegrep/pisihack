# Generated by Django 2.2.2 on 2019-06-29 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190629_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='author',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.UserProfile'),
        ),
    ]
