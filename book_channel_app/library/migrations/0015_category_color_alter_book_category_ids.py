# Generated by Django 4.0.5 on 2022-07-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_rename_category_id_book_category_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default='#FF0000', max_length=7),
        ),
        migrations.AlterField(
            model_name='book',
            name='category_ids',
            field=models.ManyToManyField(blank=True, to='library.category', verbose_name='Categories'),
        ),
    ]
