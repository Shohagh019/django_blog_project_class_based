# Generated by Django 5.1.2 on 2024-11-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_image_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_time',
            new_name='created_on',
        ),
    ]
