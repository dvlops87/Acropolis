# Generated by Django 3.2.4 on 2021-06-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]