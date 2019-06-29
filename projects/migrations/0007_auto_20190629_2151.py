# Generated by Django 2.2.2 on 2019-06-29 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190629_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_profile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.TextField(max_length=3092),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]