# Generated by Django 5.2 on 2025-04-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('NC', 'NoneCategory'), ('LD', 'Landscape'), ('UB', 'Urban'), ('MC', 'Macro'), ('AS', 'Artisctic')], default='NC', max_length=2),
        ),
    ]
