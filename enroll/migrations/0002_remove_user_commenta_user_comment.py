# Generated by Django 4.0.2 on 2022-07-15 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='commenta',
        ),
        migrations.AddField(
            model_name='user',
            name='comment',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]