# Generated by Django 3.0.5 on 2020-05-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='ends',
            field=models.CharField(max_length=25, null=True, verbose_name='Interview Ends Date'),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='starts',
            field=models.CharField(max_length=25, null=True, verbose_name='Interview Date'),
        ),
    ]