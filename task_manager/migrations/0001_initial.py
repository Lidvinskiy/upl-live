# Generated by Django 3.2.6 on 2021-10-20 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Tag')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MEDIUM', max_length=64)),
                ('status', models.CharField(choices=[('BACKLOG', 'Backlog'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='IN_PROGRESS', max_length=64)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(related_name='task', to='task_manager.Tag')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]