# Generated by Django 3.2.4 on 2021-06-30 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_blog_commnet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blogCon',
            new_name='blog',
        ),
    ]