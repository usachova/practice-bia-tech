# Generated by Django 4.0.4 on 2022-06-13 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_article_author_article_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.topic', verbose_name='тема'),
        ),
    ]