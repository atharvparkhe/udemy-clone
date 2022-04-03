# Generated by Django 4.0.2 on 2022-02-28 04:00

import app.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=50)),
                ('category_img', models.ImageField(upload_to='categories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='courses')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('ratings', models.FloatField(default=0, validators=[app.validators.validate_stars])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_category', to='app.categorymodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_section', to='app.coursemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('sub_cat_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopicModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('video', models.URLField(max_length=250)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_topic', to='app.sectionmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_sub_category', to='app.subcategorymodel'),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher', to='authentication.teachermodel'),
        ),
    ]