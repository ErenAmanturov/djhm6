# Generated by Django 4.1.1 on 2022-09-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_stars_post_type_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(1, 'Animals'), (2, 'Cars'), (3, 'Recipes'), (4, 'Nature'), (5, 'Other')], null=True),
        ),
    ]
