# Generated by Django 3.0.5 on 2023-08-12 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_post_updation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auther',
            name='email',
        ),
        migrations.RemoveField(
            model_name='auther',
            name='name',
        ),
        migrations.RemoveField(
            model_name='auther',
            name='password',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_private',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updation_date',
        ),
    ]