# Generated by Django 4.0.5 on 2022-07-17 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_category_remove_book_category_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.category'),
        ),
    ]
