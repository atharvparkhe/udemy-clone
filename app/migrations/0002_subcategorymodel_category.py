# Generated by Django 4.0.2 on 2022-02-28 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorymodel',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='app.categorymodel'),
            preserve_default=False,
        ),
    ]