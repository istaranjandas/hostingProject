# Generated by Django 3.2.17 on 2023-04-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformid',
            name='codechefID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformid',
            name='codeforcesID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformid',
            name='hackerRankID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformid',
            name='leetcodeID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformid',
            name='spojID',
            field=models.CharField(default='', max_length=100),
        ),
    ]