# Generated by Django 2.2.2 on 2019-07-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='visibility',
            field=models.SmallIntegerField(choices=[(1, 'Public'), (2, 'Private')], default=1),
        ),
    ]
