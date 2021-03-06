# Generated by Django 4.0.2 on 2022-02-22 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='What is the name of this feed', max_length=200, verbose_name='Feed Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name'])),
                ('link', models.URLField(help_text='Copy the url of the rss feed you want to subscribe to and paste it here', max_length=1000, verbose_name='RSS Feed Url')),
                ('number_of_update_posts', models.PositiveSmallIntegerField(help_text='How many latest posts should be fetched from the feed at the interval specified', verbose_name='Number of Latest Updates')),
                ('email', models.EmailField(help_text='Which email should we send your news feed updates to?', max_length=300, verbose_name='Email Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL, verbose_name='Owner of Feed')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
