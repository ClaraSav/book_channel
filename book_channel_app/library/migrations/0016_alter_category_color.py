# Generated by Django 4.0.5 on 2022-08-03 02:38

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_category_color_alter_book_category_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=colorfield.fields.ColorField(default='#00FF00', image_field=None, max_length=18, samples=None),
        ),
    ]
