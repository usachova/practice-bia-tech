# Generated by Django 4.0.4 on 2022-06-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_alter_article_options_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='изображение'),
        ),
    ]