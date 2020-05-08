# Generated by Django 3.0.5 on 2020-05-08 20:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_questions', '0002_auto_20200508_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(verbose_name=datetime.datetime(2020, 5, 8, 20, 7, 41, 554447, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(max_length=300)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2020, 5, 8, 20, 7, 41, 551446, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post_questions.PostQuestion'),
        ),
    ]
