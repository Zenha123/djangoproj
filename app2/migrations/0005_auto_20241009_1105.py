# Generated by Django 3.2.25 on 2024-10-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_alter_movieinfo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]