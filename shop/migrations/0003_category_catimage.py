# Generated by Django 2.2 on 2020-07-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_ratingmodel_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catimage',
            field=models.ImageField(blank=True, upload_to='category/%Y/%m/%d'),
        ),
    ]