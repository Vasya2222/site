# Generated by Django 5.0 on 2023-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='blog/image')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
