# Generated by Django 5.0.7 on 2024-08-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0005_alter_category_options_alter_joke_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(to='jokes.tag'),
        ),
    ]
