# Generated by Django 3.2.4 on 2021-07-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_blogcon_comment_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='answer',
            field=models.CharField(default='', max_length=10),
        ),
    ]