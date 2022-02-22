from django.contrib import admin

from .models import Feed, Entry


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "number_of_update_posts"]


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]
