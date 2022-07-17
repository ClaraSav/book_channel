# Generated by Django 4.0.5 on 2022-07-16 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='languaje_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library.languaje', verbose_name='Languaje'),
        ),
        migrations.AddField(
            model_name='book',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.category', verbose_name='Category'),
        ),
    ]