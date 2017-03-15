from django.contrib import admin
from .models import story, comment


class StoryAdmin(admin.ModelAdmin):
	list_display = ('author','story_title', 'date')
	search_fields = ('author', 'story_title', 'genre', 'content')
admin.site.register(story, StoryAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'story','created','active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email','body')
admin.site.register(comment, CommentAdmin)