# Generated by Django 3.2 on 2022-05-31 05:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email_Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=222)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('img', models.ImageField(upload_to='Recources')),
                ('note', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'RESOURCES',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='')),
                ('designation', models.CharField(max_length=250)),
                ('twitter', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=66)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='Recources')),
                ('img1', models.ImageField(blank=True, upload_to='Recources')),
                ('img2', models.ImageField(blank=True, upload_to='Recources')),
                ('img3', models.ImageField(blank=True, upload_to='Recources')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.res')),
            ],
            options={
                'verbose_name_plural': 'RESOURCES IMAGES',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Blog/Pics')),
                ('title', models.CharField(max_length=450)),
                ('name', models.CharField(max_length=222)),
                ('sub_text', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
                ('content', ckeditor.fields.RichTextField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b.category')),
            ],
        ),
    ]
