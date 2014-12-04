from django.contrib import admin
from music.models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('name', 'url')
	search_fields = ('name', 'artist')

admin.site.register(Track, TrackAdmin)