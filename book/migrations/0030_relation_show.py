# Generated by Django 5.0.3 on 2024-05-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0029_commentvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]