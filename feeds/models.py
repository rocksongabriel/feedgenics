from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import AutoSlugField


User = settings.AUTH_USER_MODEL


class Feed(models.Model):
    name = models.CharField(
        verbose_name=_("Feed Name"),
        help_text="What is the name of this feed",
        max_length=200,
        blank=False,
        null=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from=["name"])
    owner = models.ForeignKey(
        User,
        verbose_name=_("Owner of Feed"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="feeds",
    )
    link = models.URLField(
        verbose_name=_("RSS Feed Url"),
        help_text="Copy the url of the rss feed you want to subscribe to and paste it here",
        max_length=1000,
        blank=False,
        null=False,
    )
    number_of_update_posts = models.PositiveSmallIntegerField(
        verbose_name=_("Number of Latest Updates"),
        help_text="How many latest posts should be fetched from the feed at the interval specified",
    )
    email = models.EmailField(
        verbose_name=_("Email Address"),
        help_text="Which email should we send your news feed updates to?",
        blank=False,
        null=False,
        max_length=300,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "-created",
        ]
