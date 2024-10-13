# Generated by Django 3.2.25 on 2024-10-10 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_auto_20241009_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10)),
                ('certified_by', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='censor_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='app2.censorinfo'),
        ),
    ]