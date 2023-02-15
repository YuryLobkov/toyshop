# Generated by Django 4.1.7 on 2023-02-15 16:35

from django.db import migrations, models
import django.db.models.deletion
import showcase.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('in_stock', models.BooleanField()),
                ('quantity', models.PositiveIntegerField()),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Post slug')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=showcase.models.path_and_rename)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.categories')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.materials')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.sizes')),
            ],
        ),
    ]
