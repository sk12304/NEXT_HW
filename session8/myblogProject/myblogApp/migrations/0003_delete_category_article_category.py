# Generated by Django 4.1.7 on 2023-04-06 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogApp', '0002_category_article_view_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
