# Generated by Django 3.2.25 on 2024-10-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_auto_20241010_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='directed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dirmovie', to='app2.director'),
        ),
    ]
