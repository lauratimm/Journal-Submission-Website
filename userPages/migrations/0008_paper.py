# Generated by Django 3.0.4 on 2020-04-14 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userPages', '0007_auto_20200413_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(max_length=10)),
                ('upload_date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paper_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
