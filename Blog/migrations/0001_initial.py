# Generated by Django 3.1.5 on 2021-01-11 15:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=30)),
                ('blog_content', models.TextField(default='', max_length=5000)),
                ('blog_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('blog_author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-blog_date',),
            },
        ),
        migrations.CreateModel(
            name='BlogPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=20)),
                ('comment_date', models.DateField(blank=True, null=True)),
                ('comment_time', models.TimeField(blank=True, null=True)),
                ('blog', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Blog.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=250)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
