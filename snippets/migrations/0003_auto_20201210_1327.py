# Generated by Django 3.1.4 on 2020-12-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='style',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('c', 'C'), ('c++', 'C++'), ('javascript', 'Javascript')], default='python', max_length=100),
        ),
    ]
