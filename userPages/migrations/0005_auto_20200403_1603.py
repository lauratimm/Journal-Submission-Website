# Generated by Django 3.0.4 on 2020-04-03 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('userPages', '0004_auto_20200403_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='proposal_id',
            new_name='proposal',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reviewer_id',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='journal_id',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='paper_id',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='proposal_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_reviewer', to='home.User'),
        ),
    ]