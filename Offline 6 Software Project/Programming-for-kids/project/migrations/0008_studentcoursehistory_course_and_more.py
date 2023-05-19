# Generated by Django 4.1.7 on 2023-02-28 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_programmingproblem_problem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursehistory',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.course'),
        ),
        migrations.AddField(
            model_name='studentcoursehistory',
            name='mcq_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentcoursehistory',
            name='prog_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentcoursehistory',
            name='reading_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentcoursehistory',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.weeklymodules'),
        ),
        migrations.AddField(
            model_name='weeklymodules',
            name='contents',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
