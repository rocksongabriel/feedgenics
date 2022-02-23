# Generated by Django 4.0.2 on 2022-02-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField()),
                ('title', models.CharField(max_length=500, verbose_name='Title of Entry')),
                ('link', models.URLField(max_length=600, verbose_name='Link to Post')),
                ('summary', models.TextField(blank=True, null=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='feeds.feed')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]