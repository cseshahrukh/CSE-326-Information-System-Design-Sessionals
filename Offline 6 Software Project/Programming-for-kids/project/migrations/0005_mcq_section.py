# Generated by Django 4.1.7 on 2023-02-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_readingmaterial_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.readingmaterial'),
        ),
    ]
