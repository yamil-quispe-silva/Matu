# Generated by Django 4.2.8 on 2024-01-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/images'),
        ),
    ]