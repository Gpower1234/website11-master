# Generated by Django 3.0.5 on 2023-03-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20230324_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogbank',
            name='category',
            field=models.CharField(choices=[('Spiritual Blog', 'Spiritual Blog'), ('Dating Blog', 'Dating Blog'), ('Love Blog', 'Love Blog'), ('Friends Blog', 'Friends Blog'), ('Fashion Blog', 'Fashion Blog'), ('Food Blog', 'Food Blog'), ('Travel Blog', 'Travel Blog'), ('Music Blog', 'Music Blog'), ('Lifestyle Blog', 'Lifestyle Blog'), ('Fitness Blog', 'Fitness Blog'), ('DIY Blog', 'DIY Blog'), ('Sports Blog', 'Sports Blog'), ('Finance Blog', 'Finance Blog'), ('Political Blog', 'Political Blog'), ('Parenting Blog', 'Parenting Blog'), ('Business Blog', 'Business Blog'), ('Personal Blog', 'Personal Blog'), ('Movie Blog', 'Movie Blog'), ('Car Blog', 'Car Blog'), ('News Blog', 'News Blog'), ('Pet Blog', 'Pet Blog'), ('Gaming Blog', 'Gaming Blog'), ('Technology Blog', 'Technology Blog'), ('Religious Blog', 'Religious Blog'), ('Story Blog', 'Story Blog'), ('Blog', 'Blog')], default='Blog', max_length=20, null=True, verbose_name='Blog About'),
        ),
    ]