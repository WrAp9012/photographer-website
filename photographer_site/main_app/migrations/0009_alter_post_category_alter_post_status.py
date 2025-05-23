# Generated by Django 5.2 on 2025-04-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('NC', 'NoneCategory'), ('LD', 'Landscape'), ('UB', 'Urban'), ('MC', 'Macro'), ('AS', 'Artisctic')], default='NC', max_length=12),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
    ]
