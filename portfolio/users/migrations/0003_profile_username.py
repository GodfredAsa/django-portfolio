# Generated by Django 4.1 on 2022-08-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_username_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]